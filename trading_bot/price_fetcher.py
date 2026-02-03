"""
Price Fetcher - Get live crypto prices
Supports: NonKYC, DexScreener, CoinGecko
"""

import requests
import json
import time

class PriceFetcher:
    def __init__(self):
        self.cache = {}
        self.cache_time = 30  # seconds
    
    def get_price(self, symbol=None):
        """Get price for symbol - tries multiple sources"""
        if symbol is None:
            from config import get_config
            config = get_config()
            symbol = config.get('symbol', 'SHIB/USDT')
        
        # Try NonKYC first
        price = self.get_nonkyc_price(symbol)
        if price:
            return price
        
        # Fallback to DexScreener
        price = self.get_dexscreener_price(symbol)
        if price:
            return price
        
        # Fallback to CoinGecko
        price = self.get_coingecko_price(symbol)
        if price:
            return price
        
        return None
    
    def get_nonkyc_price(self, symbol):
        """Get price from NonKYC exchange"""
        try:
            # NonKYC API endpoint for price
            url = f"https://nonkyc.io/api/v1/market/{symbol.replace('/', '_')}/ticker"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'last' in data:
                    return float(data['last'])
        except Exception as e:
            print(f"NonKYC API error: {e}")
        
        return None
    
    def get_dexscreener_price(self, symbol):
        """Get price from DexScreener"""
        try:
            # DexScreener API
            pair_address = self.get_dexscreener_pair(symbol)
            if pair_address:
                url = f"https://api.dexscreener.com/latest/dex/pairs/{pair_address}"
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if 'pair' in data and 'priceUsd' in data['pair']:
                        return float(data['pair']['priceUsd'])
        except Exception as e:
            print(f"DexScreener API error: {e}")
        
        return None
    
    def get_dexscreener_pair(self, symbol):
        """Get DexScreener pair address for symbol"""
        pair_map = {
            'SHIB/USDT': '0x58583c0c3553f60c2323f8503c6f1c0729c45c84',
            'PEPEW/USDT': '0x...',  # Add actual pair address
        }
        return pair_map.get(symbol)
    
    def get_coingecko_price(self, symbol):
        """Get price from CoinGecko"""
        try:
            # Map symbol to CoinGecko ID
            id_map = {
                'SHIB/USDT': 'shiba-inu',
                'PEPEW/USDT': None,  # Not on CoinGecko
            }
            
            coin_id = id_map.get(symbol)
            if not coin_id:
                return None
            
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if coin_id in data and 'usd' in data[coin_id]:
                    return float(data[coin_id]['usd'])
        except Exception as e:
            print(f"CoinGecko API error: {e}")
        
        return None
    
    def get_orderbook(self, symbol):
        """Get orderbook for symbol"""
        try:
            url = f"https://nonkyc.io/api/v1/market/{symbol.replace('/', '_')}/orderbook"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Orderbook error: {e}")
        
        return None
    
    def get_balance(self, api_key, api_secret):
        """Get account balance from NonKYC"""
        try:
            # This would require proper NonKYC API authentication
            headers = {
                'X-API-Key': api_key,
                'X-API-Secret': api_secret
            }
            url = "https://nonkyc.io/api/v1/balance"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Balance error: {e}")
        
        return None


if __name__ == '__main__':
    fetcher = PriceFetcher()
    
    # Test prices
    symbols = ['SHIB/USDT', 'PEPEW/USDT']
    
    for symbol in symbols:
        price = fetcher.get_price(symbol)
        if price:
            print(f"{symbol}: ${price}")
        else:
            print(f"{symbol}: Price not available")
