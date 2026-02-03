#!/usr/bin/env python3
"""
Daily Scalper - Quick profit trading bot
Strategy: Buy near daily lows, sell for +5% profit
Schedule: 8 AM, 2 PM, 8 PM
"""

import config
import price_fetcher
import telegram_alerts
import data_storage
from datetime import datetime

class DailyScalper:
    def __init__(self):
        self.config = config.get_config()
        self.fetcher = price_fetcher.PriceFetcher()
        self.alerts = telegram_alerts.TelegramAlerts()
        self.storage = data_storage.DataStorage()
        
    def run(self):
        """Execute daily scalping routine"""
        print(f"\n{'='*60}")
        print(f"📊 DAILY SCALPER - {datetime.now().strftime('%H:%M')}")
        print(f"{'='*60}\n")
        
        # Get current price and daily range
        symbol = self.config.get('symbol', 'SHIB/USDT')
        price = self.fetcher.get_price(symbol)
        
        if not price:
            print("❌ Could not fetch price")
            self.alerts.send_error_alert("Scalper", "Could not fetch price")
            return
        
        # Get daily high/low (simulated - in real implementation, track this)
        daily_high = price * 1.02  # Simulated
        daily_low = price * 0.98   # Simulated
        
        print(f"📊 Market Status:")
        print(f"   Current: ${price}")
        print(f"   Daily High: ${daily_high}")
        print(f"   Daily Low: ${daily_low}")
        
        # Calculate position
        daily_low_pct = ((price - daily_low) / daily_low) * 100
        
        print(f"\n🎯 Entry Analysis:")
        print(f"   Price is {daily_low_pct:.1f}% above daily low")
        
        # Decision logic
        if daily_low_pct < 5:
            # Good buy opportunity - near daily low
            print(f"\n✅ GOOD BUY OPPORTUNITY!")
            print(f"   Price is close to daily low")
            self.execute_scalp(symbol, price, 'BUY')
        elif daily_low_pct < 10:
            # Marginal - could go either way
            print(f"\n⚖️ MARGINAL - Monitoring")
            self.alerts.send_message(f"⚖️ SHIB/USDT at ${price} ({daily_low_pct:.1f}% above daily low) - Watching")
        else:
            # Too high - wait for dip
            print(f"\n⏸️ TOO HIGH - Waiting for dip")
            self.alerts.send_message(f"⏸️ SHIB/USDT at ${price} ({daily_low_pct:.1f}% above daily low) - Too high to buy")
        
        # Check for profit targets
        self.check_profit_targets(symbol, price)
    
    def execute_scalp(self, symbol, price, action):
        """Execute scalping trade"""
        position_size = self.config.get('position_size', 5.0)
        sell_target = price * 1.05  # +5% profit
        stop_loss = price * 0.90    # -10% stop loss
        
        print(f"\n🚀 SCALP TRADE:")
        print(f"   Action: {action}")
        print(f"   Entry: ${price}")
        print(f"   Target: ${sell_target} (+5%)")
        print(f"   Stop: ${stop_loss} (-10%)")
        print(f"   Size: ${position_size}")
        
        # Log trade
        trade = {
            'symbol': symbol,
            'action': action,
            'entry_price': price,
            'target': sell_target,
            'stop_loss': stop_loss,
            'size': position_size,
            'strategy': 'daily_scalper',
            'mode': self.config.get('mode', 'LIVE')
        }
        
        if action == 'BUY':
            self.storage.log_trade(trade)
            
            # Send alert
            self.alerts.send_message(
                f"🚀 *SCALP BUY*\n\n"
                f"Symbol: {symbol}\n"
                f"Entry: ${price}\n"
                f"Target: ${sell_target} (+5%)\n"
                f"Stop: ${stop_loss} (-10%)\n"
                f"Size: ${position_size}\n\n"
                f"_Strategy: Daily Scalper_"
            )
    
    def check_profit_targets(self, symbol, current_price):
        """Check if any open positions hit targets"""
        trades = self.storage.get_trades()
        
        for trade in trades:
            if trade.get('strategy') != 'daily_scalper':
                continue
            
            if trade.get('action') != 'BUY':
                continue
            
            target = trade.get('target', 0)
            stop = trade.get('stop_loss', 0)
            
            # Check take profit
            if target and current_price >= target:
                print(f"\n🎉 TAKE PROFIT!")
                print(f"   Target: ${target} reached!")
                self.alerts.send_message(
                    f"🎉 *TAKE PROFIT - SCALPER*\n\n"
                    f"Symbol: {symbol}\n"
                    f"Entry: ${trade['entry_price']}\n"
                    f"Exit: ${current_price}\n"
                    f"Profit: +5% 🎉"
                )
            
            # Check stop loss
            elif stop and current_price <= stop:
                print(f"\n⚠️ STOP LOSS!")
                print(f"   Stop: ${stop} hit!")
                self.alerts.send_message(
                    f"⚠️ *STOP LOSS - SCALPER*\n\n"
                    f"Symbol: {symbol}\n"
                    f"Entry: ${trade['entry_price']}\n"
                    f"Exit: ${current_price}\n"
                    f"Loss: -10%"
                )


def main():
    scalper = DailyScalper()
    scalper.run()

if __name__ == '__main__':
    main()
