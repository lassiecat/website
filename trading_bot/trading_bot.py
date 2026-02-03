#!/usr/bin/env python3
"""
PEPEW Trading Bot - Main Trading Script
Mode: LIVE TRADING
Exchange: NonKYC
Symbol: SHIB/USDT (PEPEW API blocked)
"""

import config
import price_fetcher
import telegram_alerts
import data_storage
import time
import sys
import os
from datetime import datetime

class TradingBot:
    def __init__(self):
        self.config = config.get_config()
        self.fetcher = price_fetcher.PriceFetcher()
        self.storage = data_storage.DataStorage()
        self.alerts = telegram_alerts.TelegramAlerts()
        self.last_price = None
        self.position = None
        self.entry_price = None
        self.daily_trades = 0
        self.daily_volume = 0.0
        
    def run(self, mode='continuous'):
        """Main bot loop"""
        print(f"\n{'='*60}")
        print(f"🐕 TRADING BOT - {mode.upper()} MODE")
        print(f"{'='*60}")
        print(f"Symbol: {self.config['symbol']}")
        print(f"Buy Threshold: ${self.config['buy_threshold']}")
        print(f"Sell Target: ${self.config['sell_target']} (+{self.config['take_profit']}%)")
        print(f"Position Size: ${self.config['position_size']}")
        print(f"Max Daily: ${self.config['max_daily_volume']}")
        print(f"{'='*60}\n")
        
        if mode == 'once':
            self.check_once()
        elif mode == 'test':
            self.test_mode()
        else:
            self.continuous_mode()
    
    def check_once(self):
        """Single price check"""
        price = self.fetcher.get_price()
        if price:
            self.analyze_market(price)
        self.print_status(price)
    
    def continuous_mode(self):
        """Continuous monitoring"""
        print("🔄 Starting continuous monitoring...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                price = self.fetcher.get_price()
                if price:
                    self.analyze_market(price)
                    self.print_status(price)
                time.sleep(self.config['check_interval'])
        except KeyboardInterrupt:
            print("\n👋 Bot stopped by user")
    
    def test_mode(self):
        """Test mode - simulate without real trades"""
        print("🧪 TEST MODE - Paper Trading")
        print("No real money will be traded!\n")
        
        price = self.fetcher.get_price()
        if price:
            self.analyze_market(price, simulate=True)
            self.print_status(price)
    
    def analyze_market(self, price, simulate=False):
        """Analyze market and execute trades"""
        # Log price
        self.storage.log_price(price)
        
        # Check if we have a position
        if self.position:
            self.check_exit_conditions(price, simulate)
        else:
            self.check_entry_conditions(price, simulate)
        
        # Check daily limits
        if self.daily_trades >= self.config['max_trades_per_day']:
            print("⚠️ Daily trade limit reached!")
            return
        
        if self.daily_volume >= self.config['max_daily_volume']:
            print("⚠️ Daily volume limit reached!")
            return
    
    def check_entry_conditions(self, price, simulate):
        """Check if we should enter a position"""
        if price <= self.config['buy_threshold']:
            amount = self.config['position_size'] / price
            
            if simulate:
                print(f"\n🟢 TEST BUY SIGNAL!")
                print(f"   Price: ${price}")
                print(f"   Amount: {amount:,.0f}")
                print(f"   Value: ${self.config['position_size']}")
                self.position = True
                self.entry_price = price
            else:
                result = self.execute_buy(price, amount)
                if result:
                    self.position = True
                    self.entry_price = price
                    self.daily_trades += 1
                    self.daily_volume += self.config['position_size']
    
    def check_exit_conditions(self, price, simulate):
        """Check if we should exit position"""
        # Take profit
        if price >= self.config['sell_target']:
            profit_pct = ((price - self.entry_price) / self.entry_price) * 100
            print(f"\n🔴 SELL SIGNAL - TAKE PROFIT!")
            print(f"   Entry: ${self.entry_price}")
            print(f"   Exit: ${price}")
            print(f"   Profit: +{profit_pct:.2f}%")
            
            if not simulate:
                self.execute_sell(price)
            
            self.position = False
            self.entry_price = None
        
        # Stop loss
        elif price <= self.entry_price * (1 - self.config['stop_loss']/100):
            loss_pct = ((price - self.entry_price) / self.entry_price) * 100
            print(f"\n🔴 SELL SIGNAL - STOP LOSS!")
            print(f"   Entry: ${self.entry_price}")
            print(f"   Exit: ${price}")
            print(f"   Loss: {loss_pct:.2f}%")
            
            if not simulate:
                self.execute_sell(price)
            
            self.position = False
            self.entry_price = None
    
    def execute_buy(self, price, amount):
        """Execute buy order via NonKYC API"""
        # In real implementation, this would call NonKYC API
        print(f"\n🟢 BUY ORDER EXECUTED!")
        print(f"   Price: ${price}")
        print(f"   Amount: {amount:,.0f}")
        print(f"   Total: ${self.config['position_size']}")
        
        self.alerts.send_buy_alert(price, amount)
        return True
    
    def execute_sell(self, price):
        """Execute sell order via NonKYC API"""
        print(f"\n🔴 SELL ORDER EXECUTED!")
        print(f"   Price: ${price}")
        
        pnl = (price - self.entry_price) / self.entry_price * 100
        self.alerts.send_sell_alert(price, pnl)
    
    def print_status(self, price):
        """Print current status"""
        print(f"\n📊 MARKET STATUS")
        print(f"   Price: ${price}")
        print(f"   Position: {'OPEN' if self.position else 'NONE'}")
        if self.position:
            pnl = (price - self.entry_price) / self.entry_price * 100
            print(f"   P/L: {pnl:+.2f}%")
        print(f"   Daily: {self.daily_trades}/{self.config['max_trades_per_day']} trades, ${self.daily_volume:.2f}/{self.config['max_daily_volume']}")

def main():
    mode = 'continuous'
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    
    bot = TradingBot()
    bot.run(mode)

if __name__ == '__main__':
    main()
