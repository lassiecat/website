"""
Trading Bot Configuration
⚠️ IMPORTANT: Keep this file secure!
Never commit to version control!
"""

# NonKYC Exchange API
NONKYC = {
    "api_key": "c677d4108806428c97a89a0e31597029",
    "api_secret": "7bd6623182d9b7f96eee360cb1d12b700941cb7b",
    "base_url": "https://nonkyc.io/api/v1",
    "enabled": True
}

# Telegram Alerts Configuration
TELEGRAM = {
    "bot_token": "8396730713:AAETb_miSVW7H_rUlk4Fl_p-Q06WuKrm-2Y",
    "chat_id": "6404339546",
    "enabled": True
}

# Trading Configuration
TRADING = {
    # Symbol to trade (SHIB/USDT - PEPEW API blocked!)
    "symbol": "SHIB/USDT",
    
    # Trading mode: TEST or LIVE
    "mode": "LIVE",
    
    # Buy when price drops below this
    "buy_threshold": 0.00000600,
    
    # Sell when price rises above this
    "sell_target": 0.00000720,
    
    # Position size per trade (USD)
    "position_size": 5.00,
    
    # Daily limits
    "max_trades_per_day": 5,
    "max_daily_volume": 5.00,
    
    # Risk management
    "stop_loss": 10.0,      # Sell if -10% loss
    "take_profit": 20.0,    # Sell if +20% gain
    "trailing_stop": 10.0,  # Trailing stop percentage
    
    # Check interval (seconds)
    "check_interval": 300,  # 5 minutes
    
    # Require manual confirmation for LIVE trades
    "require_confirmation": False
}

# PEPEW Masternode Settings (monitor only)
PEPEW = {
    "masternode_address": "P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj",
    "balance": 46105088,
    "explorer_url": "https://explorer.pepepow.org/address/P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj",
    "website": "https://pepepow.org/",
    "api_excluded": True  # API trading disabled!
}

def get_config():
    """Return merged configuration"""
    config = {}
    config.update(NONKYC)
    config.update(TELEGRAM)
    config.update(TRADING)
    config['symbol'] = TRADING['symbol']
    config['buy_threshold'] = TRADING['buy_threshold']
    config['sell_target'] = TRADING['sell_target']
    config['position_size'] = TRADING['position_size']
    config['max_trades_per_day'] = TRADING['max_trades_per_day']
    config['max_daily_volume'] = TRADING['max_daily_volume']
    config['stop_loss'] = TRADING['stop_loss']
    config['take_profit'] = TRADING['take_profit']
    config['check_interval'] = TRADING['check_interval']
    config['require_confirmation'] = TRADING['require_confirmation']
    config['mode'] = TRADING['mode']
    return config

if __name__ == '__main__':
    config = get_config()
    print("Current Configuration:")
    for key, value in config.items():
        if key not in ['api_key', 'api_secret', 'bot_token']:
            print(f"  {key}: {value}")
