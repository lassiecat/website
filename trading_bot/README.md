# 🐕 Trading Bot

Automated trading bot for SHIB/USDT on NonKYC exchange.

## ⚠️ Important: PEPEW API Blocked

**NonKYC has `apiExcluded: true` for PEPEW/USDT** - API trading is disabled!

This bot trades **SHIB/USDT** which does support API trading.

---

## 📁 Files

```
trading_bot/
├── trading_bot.py      # Main trading bot (continuous mode)
├── daily_scalper.py   # Quick +5% profit scalping
├── auto_trader.py     # Auto-adjusts strategy daily
├── pepew_price.py     # PEPEW price fetcher (Playwright-stealth)
├── price_fetcher.py   # Live price fetching
├── config.py          # API keys & configuration
├── telegram_alerts.py # Telegram notifications
├── data_storage.py    # CSV logging & history
└── data/
    ├── price_history.csv
    ├── alerts.log
    └── trades.json
```

---

## 🚀 Quick Start

```bash
cd /Users/maxwell/.openclaw/workspace/trading_bot

# Install dependencies
pip install requests playwright
playwright install chromium

# Test mode (paper trading)
python3 trading_bot.py --test

# Single check
python3 trading_bot.py --once

# Continuous mode (LIVE TRADING)
python3 trading_bot.py

# Daily scalper
python3 daily_scalper.py

# Auto-adjust strategy
python3 auto_trader.py

# PEPEW price fetch
python3 pepew_price.py
```

---

## ⚙️ Configuration

Edit `config.py` to update:

```python
# Trading Settings
"symbol": "SHIB/USDT",           # Trading pair
"buy_threshold": 0.00000600,     # Buy below this
"sell_target": 0.00000720,        # Sell above this (+20%)
"position_size": 5.00,           # $ per trade
"max_daily_volume": 5.00,        # $ max per day
"stop_loss": 10.0,               # -10% stop loss
"take_profit": 20.0,             # +20% take profit
```

---

## 📱 Telegram Alerts

Bot: @pepew_alert_bot

Alerts include:
- 🔔 Buy/Sell signals
- 📊 Price updates
- 🎉 Profit notifications
- ⚠️ Error alerts

---

## ⏰ Cron Jobs

Add to crontab (`crontab -e`):

```bash
# Morning scalper (8 AM)
0 8 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 daily_scalper.py

# Mid-day review (2 PM)
0 14 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 auto_trader.py

# Evening review (6 PM)
0 18 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 auto_trader.py

# Trading check (every 4 hours)
0 */4 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 trading_bot.py --once
```

---

## 📊 Portfolio

### PEPEW Holdings (Masternode)
- **Address:** P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj
- **Balance:** 46,105,088 PEPEW
- **Value:** ~$19.73
- **Explorer:** https://explorer.pepepow.org/address/P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj

### SHIB Trading Balance
- **USDT:** $13.73

---

## ⚠️ Risk Warnings

1. **API Trading Disabled for PEPEW** - Cannot auto-trade PEPEW via API
2. **Live Trading** - Real money at risk
3. **Small Daily Limit** - Max $5/day limits losses
4. **Crypto Volatility** - Prices can move rapidly
5. **Stop Losses** - Auto-sell at -10%

---

## 🔑 API Credentials

**NonKYC Exchange:**
- API Key: `c677d4108806428c97a89a0e31597029`
- API Secret: `7bd6623182d9b7f96eee360cb1d12b700941cb7b`

**Telegram:**
- Bot Token: `8396730713:AAETb_miSVW7H_rUlk4Fl_p-Q06WuKrm-2Y`
- Chat ID: `6404339546`

---

## 📈 Historical Performance

| Date | Value | Change |
|------|-------|--------|
| Jan 28 | $16.14 | - |
| Feb 03 | $19.73 | +$3.60 (+22.29%) |

---

## 🛠️ Troubleshooting

### "API trading disabled for PEPEW"
✅ Normal - Use SHIB/USDT instead

### "Could not fetch price"
- Check internet connection
- Try again in a few seconds
- NonKYC may have rate limits

### Telegram not working
- Check bot token is correct
- Bot must be started with /start
- Chat ID must be numeric

---

## 📚 Dependencies

```bash
pip install requests
pip install playwright
playwright install chromium
```

---

**Bot Status:** 🔴 LIVE TRADING
**Symbol:** SHIB/USDT
**Max Daily:** $5.00
