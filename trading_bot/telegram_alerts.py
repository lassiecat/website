"""
Telegram Alerts - Send notifications to Telegram
Bot: @pepew_alert_bot
"""

import requests
import json
from datetime import datetime

class TelegramAlerts:
    def __init__(self):
        from config import get_config
        config = get_config()
        
        self.bot_token = config.get('bot_token')
        self.chat_id = config.get('chat_id')
        self.enabled = config.get('enabled', True)
        
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
    
    def send_message(self, text, parse_mode='Markdown'):
        """Send message to Telegram"""
        if not self.enabled:
            print(f"📱 Telegram disabled - would send: {text}")
            return False
        
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': text,
                'parse_mode': parse_mode
            }
            response = requests.post(url, json=data, timeout=10)
            
            if response.status_code == 200:
                return True
            else:
                print(f"Telegram error: {response.text}")
                return False
        except Exception as e:
            print(f"Telegram send error: {e}")
            return False
    
    def send_price_alert(self, symbol, price, change_pct):
        """Send price alert"""
        emoji = "📈" if change_pct > 0 else "📉"
        text = f"{emoji} *{symbol} PRICE ALERT*\n\n"
        text += f"Current: ${price}\n"
        text += f"24h Change: {change_pct:+.2f}%"
        
        return self.send_message(text)
    
    def send_buy_alert(self, price, amount):
        """Send buy order alert"""
        from config import get_config
        config = get_config()
        
        symbol = config.get('symbol', 'SHIB/USDT')
        value = config.get('position_size', 5.0)
        
        text = f"🟢 *BUY ORDER EXECUTED!*\n\n"
        text += f"Symbol: {symbol}\n"
        text += f"Price: ${price}\n"
        text += f"Amount: {amount:,.0f}\n"
        text += f"Value: ${value}\n\n"
        text += f"_Mode: {config.get('mode', 'LIVE')}_"
        
        return self.send_message(text)
    
    def send_sell_alert(self, price, pnl_pct):
        """Send sell order alert"""
        from config import get_config
        config = get_config()
        
        symbol = config.get('symbol', 'SHIB/USDT')
        
        emoji = "💰" if pnl_pct > 0 else "💸"
        text = f"{emoji} *SELL ORDER EXECUTED!*\n\n"
        text += f"Symbol: {symbol}\n"
        text += f"Price: ${price}\n"
        text += f"P/L: {pnl_pct:+.2f}%\n\n"
        
        if pnl_pct > 0:
            text += "🎉 Profit taken!"
        else:
            text += "⚠️ Stop loss triggered"
        
        return self.send_message(text)
    
    def send_daily_summary(self, portfolio_value, daily_pnl, trades):
        """Send daily portfolio summary"""
        emoji = "📊" if daily_pnl >= 0 else "📉"
        text = f"{emoji} *DAILY SUMMARY*\n\n"
        text += f"Portfolio: ${portfolio_value:.2f}\n"
        text += f"Daily P/L: ${daily_pnl:+.2f}\n"
        text += f"Trades: {trades}\n\n"
        text += f"_Generated at {datetime.now().strftime('%H:%M')}_"
        
        return self.send_message(text)
    
    def send_error_alert(self, error_type, message):
        """Send error notification"""
        text = f"⚠️ *BOT ERROR*\n\n"
        text += f"Type: {error_type}\n"
        text += f"Message: {message}\n\n"
        text += "_Check logs for details_"
        
        return self.send_message(text)
    
    def send_market_update(self, symbol, price, high_24h, low_24h):
        """Send market update"""
        text = f"📊 *MARKET UPDATE*\n\n"
        text += f"Symbol: {symbol}\n"
        text += f"Current: ${price}\n"
        text += f"24h High: ${high_24h}\n"
        text += f"24h Low: ${low_24h}\n\n"
        
        range_pct = ((high_24h - low_24h) / low_24h) * 100
        text += f"24h Range: {range_pct:.1f}%"
        
        return self.send_message(text)


if __name__ == '__main__':
    alerts = TelegramAlerts()
    
    # Test message
    alerts.send_message("🧪 Trading bot connected and ready!")
