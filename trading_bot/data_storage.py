"""
Data Storage - Log prices and trades to files
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path

class DataStorage:
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.price_file = self.data_dir / 'price_history.csv'
        self.alerts_file = self.data_dir / 'alerts.log'
        self.trades_file = self.data_dir / 'trades.json'
        self.portfolio_file = self.data_dir / 'portfolio.json'
        
        # Initialize files
        self._init_files()
    
    def _init_files(self):
        """Initialize storage files"""
        # Price history CSV
        if not self.price_file.exists():
            with open(self.price_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'datetime', 'symbol', 'price'])
        
        # Alerts log
        if not self.alerts_file.exists():
            self.alerts_file.touch()
        
        # Trades JSON
        if not self.trades_file.exists():
            with open(self.trades_file, 'w') as f:
                json.dump([], f)
    
    def log_price(self, price, symbol='SHIB/USDT'):
        """Log price to history"""
        try:
            with open(self.price_file, 'a', newline='') as f:
                writer = csv.writer(f)
                now = datetime.now()
                writer.writerow([
                    now.timestamp(),
                    now.strftime('%Y-%m-%d %H:%M:%S'),
                    symbol,
                    price
                ])
        except Exception as e:
            print(f"Price log error: {e}")
    
    def log_alert(self, alert_type, message):
        """Log alert to file"""
        try:
            with open(self.alerts_file, 'a') as f:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f"[{timestamp}] [{alert_type}] {message}\n")
        except Exception as e:
            print(f"Alert log error: {e}")
    
    def log_trade(self, trade):
        """Log trade to JSON file"""
        try:
            trades = self.get_trades()
            trades.append({
                'timestamp': datetime.now().timestamp(),
                'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                **trade
            })
            
            with open(self.trades_file, 'w') as f:
                json.dump(trades, f, indent=2)
        except Exception as e:
            print(f"Trade log error: {e}")
    
    def get_trades(self):
        """Get all trades from JSON file"""
        try:
            with open(self.trades_file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def get_price_history(self, limit=100):
        """Get recent price history"""
        prices = []
        try:
            with open(self.price_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    prices.append(row)
            
            return prices[-limit:]
        except:
            return []
    
    def save_portfolio(self, portfolio):
        """Save portfolio state"""
        try:
            portfolio['timestamp'] = datetime.now().timestamp()
            portfolio['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            with open(self.portfolio_file, 'w') as f:
                json.dump(portfolio, f, indent=2)
        except Exception as e:
            print(f"Portfolio save error: {e}")
    
    def get_portfolio(self):
        """Get saved portfolio state"""
        try:
            with open(self.portfolio_file, 'r') as f:
                return json.load(f)
        except:
            return None
    
    def get_statistics(self):
        """Calculate statistics from data"""
        trades = self.get_trades()
        prices = self.get_price_history(1000)
        
        stats = {
            'total_trades': len(trades),
            'winning_trades': sum(1 for t in trades if t.get('pnl', 0) > 0),
            'losing_trades': sum(1 for t in trades if t.get('pnl', 0) <= 0),
            'price_entries': len(prices),
        }
        
        # Calculate P/L
        if trades:
            total_pnl = sum(t.get('pnl', 0) for t in trades)
            stats['total_pnl'] = total_pnl
            stats['win_rate'] = stats['winning_trades'] / stats['total_trades'] * 100
        
        return stats
    
    def export_data(self, format='json'):
        """Export all data"""
        data = {
            'trades': self.get_trades(),
            'prices': self.get_price_history(10000),
            'statistics': self.get_statistics(),
            'exported_at': datetime.now().isoformat()
        }
        
        if format == 'json':
            return json.dumps(data, indent=2)
        elif format == 'csv':
            # Export prices to CSV
            lines = ['timestamp,datetime,symbol,price']
            for p in data['prices']:
                lines.append(f"{p['timestamp']},{p['datetime']},{p['symbol']},{p['price']}")
            return '\n'.join(lines)
        
        return data


if __name__ == '__main__':
    storage = DataStorage()
    
    # Test logging
    storage.log_price(0.00000653, 'SHIB/USDT')
    storage.log_alert('TEST', 'Test alert')
    
    # Get stats
    stats = storage.get_statistics()
    print(f"Statistics: {json.dumps(stats, indent=2)}")
