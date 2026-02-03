#!/usr/bin/env python3
"""
Auto-Trader - Auto-adjust trading strategy based on market conditions
Runs daily at 8 AM, 2 PM, 6 PM
"""

import config
import price_fetcher
import telegram_alerts
from datetime import datetime
import json

class AutoTrader:
    def __init__(self):
        self.config = config.get_config()
        self.fetcher = price_fetcher.PriceFetcher()
        self.alerts = telegram_alerts.TelegramAlerts()
    
    def run(self):
        """Analyze market and auto-adjust strategy"""
        print(f"\n{'='*60}")
        print(f"🔄 AUTO-TRADER - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'='*60}\n")
        
        symbol = self.config.get('symbol', 'SHIB/USDT')
        
        # Get market data
        price = self.fetcher.get_price(symbol)
        orderbook = self.fetcher.get_orderbook(symbol)
        
        if not price:
            print("❌ Could not fetch market data")
            self.alerts.send_error_alert("AutoTrader", "Could not fetch price")
            return
        
        # Calculate volatility and trend
        volatility, trend = self.analyze_market(price, orderbook)
        
        print(f"📊 Market Analysis:")
        print(f"   Price: ${price}")
        print(f"   Volatility: {volatility:.2f}%")
        print(f"   Trend: {trend}")
        
        # Auto-adjust strategy
        new_strategy = self.calculate_strategy(price, volatility, trend)
        
        print(f"\n🎯 Strategy Adjustment:")
        print(f"   Buy Threshold: ${new_strategy['buy_threshold']:.10f}")
        print(f"   Sell Target: ${new_strategy['sell_target']:.10f}")
        print(f"   Position Size: ${new_strategy['position_size']}")
        
        # Save new strategy
        self.save_strategy(new_strategy)
        
        # Send Telegram update
        self.send_strategy_update(price, volatility, trend, new_strategy)
    
    def analyze_market(self, price, orderbook):
        """Analyze market conditions"""
        # Simulate volatility calculation
        # In real implementation, use historical data
        volatility = 2.5  # Default 2.5%
        
        # Determine trend
        if volatility < 2:
            trend = "LOW - SIDEWAYS"
        elif volatility < 5:
            trend = "NORMAL - MODERATE MOVES"
        else:
            trend = "HIGH - VOLATILE"
        
        # Check orderbook for liquidity
        if orderbook:
            try:
                bids = orderbook.get('bids', [])[:5]
                asks = orderbook.get('asks', [])[:5]
                
                bid_volume = sum(float(b[1]) for b in bids if len(b) > 1)
                ask_volume = sum(float(a[1]) for a in asks if len(a) > 1)
                
                if bid_volume > ask_volume * 2:
                    trend += " (BUY PRESSURE)"
                elif ask_volume > bid_volume * 2:
                    trend += " (SELL PRESSURE)"
            except:
                pass
        
        return volatility, trend
    
    def calculate_strategy(self, price, volatility, trend):
        """Calculate optimal strategy based on market"""
        # Base settings
        base_buy_drop = 0.10   # Buy when 10% below current
        base_sell_gain = 0.30   # Sell when 30% above
        
        # Adjust based on volatility
        if volatility < 2:
            # Low volatility - tighter ranges
            buy_drop = 0.05   # 5% dip
            sell_gain = 0.20  # 20% gain
        elif volatility > 5:
            # High volatility - wider ranges
            buy_drop = 0.15   # 15% dip
            sell_gain = 0.50  # 50% gain
        else:
            # Normal volatility
            buy_drop = 0.10   # 10% dip
            sell_gain = 0.30  # 30% gain
        
        # Calculate thresholds
        buy_threshold = price * (1 - buy_drop)
        sell_target = price * (1 + sell_gain)
        
        # Adjust position size based on volatility
        base_position = self.config.get('position_size', 5.0)
        
        if volatility > 5:
            position_size = base_position * 0.5  # Smaller positions in high volatility
        else:
            position_size = base_position
        
        return {
            'buy_threshold': buy_threshold,
            'sell_target': sell_target,
            'position_size': position_size,
            'volatility': volatility,
            'trend': trend
        }
    
    def save_strategy(self, strategy):
        """Save strategy to config"""
        # Update config.py
        config_path = 'config.py'
        
        try:
            with open(config_path, 'r') as f:
                content = f.read()
            
            # Update values
            content = content.replace(
                '"buy_threshold": 0.00000600',
                f'"buy_threshold": {strategy["buy_threshold"]:.10f}'
            )
            content = content.replace(
                '"sell_target": 0.00000720',
                f'"sell_target": {strategy["sell_target"]:.10f}'
            )
            content = content.replace(
                '"position_size": 5.00',
                f'"position_size": {strategy["position_size"]}'
            )
            
            with open(config_path, 'w') as f:
                f.write(content)
            
            print("\n✅ Strategy saved to config.py")
            
        except Exception as e:
            print(f"\n⚠️ Could not save strategy: {e}")
    
    def send_strategy_update(self, price, volatility, trend, strategy):
        """Send strategy update to Telegram"""
        symbol = self.config.get('symbol', 'SHIB/USDT')
        
        message = f"📊 *DAILY STRATEGY UPDATE*\n\n"
        message += f"Symbol: {symbol}\n"
        message += f"Current Price: ${price}\n\n"
        message += f"📈 *Market Analysis*\n"
        message += f"Volatility: {volatility:.2f}%\n"
        message += f"Trend: {trend}\n\n"
        message += f"🎯 *Adjusted Strategy*\n"
        message += f"Buy Below: ${strategy['buy_threshold']:.10f}\n"
        message += f"Sell Target: ${strategy['sell_target']:.10f}\n"
        message += f"Position: ${strategy['position_size']}\n\n"
        message += f"_Updated at {datetime.now().strftime('%H:%M')}_"
        
        self.alerts.send_message(message)
    
    def get_market_summary(self):
        """Get current market summary"""
        symbol = self.config.get('symbol', 'SHIB/USDT')
        price = self.fetcher.get_price(symbol)
        
        if not price:
            return None
        
        volatility, trend = self.analyze_market(price, None)
        
        return {
            'symbol': symbol,
            'price': price,
            'volatility': volatility,
            'trend': trend,
            'buy_threshold': price * 0.90,
            'sell_target': price * 1.30
        }


def main():
    trader = AutoTrader()
    trader.run()

if __name__ == '__main__':
    main()
