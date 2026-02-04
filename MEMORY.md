# Long-Term Memory

## About Maxwell
- **Timezone:** Europe/London
- **Telegram ID:** 6404339546
- **Working Directory:** /Users/maxwell/.openclaw/workspace
- **Interests:** Crypto, Games, Gym/fitness, Coding

## OpenClaw Setup
- **Gateway:** Running on port 18789 with token auth
- **Bot:** @maxadjeisarpongbot (Telegram)
- **Primary Model:** MiniMax-M2.1
- **Fallback Model:** GLM-4.7

## PEPEW Trading Bot ⭐ CRITICAL

### ⚠️ IMPORTANT: PEPEW API Trading BLOCKED!
NonKYC has `apiExcluded: true` for PEPEW/USDT — **API trading is disabled for PEPEW!**

**Workaround:** Switched to SHIB/USDT for live API trading (fully supported).

### Bot Location
```
/Users/maxwell/.openclaw/workspace/trading_bot/
├── trading_bot.py       # Main bot (LIVE TRADING)
├── daily_scalper.py     # Quick +5% profit trades
├── auto_trader.py       # Auto-adjusts strategy daily
├── pepew_price.py      # PEPEW fetcher (Playwright-stealth)
├── price_fetcher.py     # Live price fetching
├── config.py            # API KEYS HERE
├── telegram_alerts.py   # Telegram notifications
├── data_storage.py      # CSV logging & history
└── data/
    ├── price_history.csv
    ├── alerts.log
    └── trades.json
```

### API Credentials (🔐 SENSITIVE)
```python
# NonKYC Exchange
NONKYC = {
    "api_key": "c677d4108806428c97a89a0e31597029",
    "api_secret": "7bd6623182d9b7f96eee360cb1d12b700941cb7b",
    "enabled": True
}

# Telegram Alerts
TELEGRAM = {
    "bot_token": "8396730713:AAETb_miSVW7H_rUlk4Fl_p-Q06WuKrm-2Y",
    "chat_id": "6404339546",
    "enabled": True
}
```
- Exchange: https://nonkyc.io/market/PEPEW_USDT
- Telegram Bot: @pepew_alert_bot

### SHIB/USDT Trading (Live)
| Metric | Value |
|--------|-------|
| Symbol | SHIB/USDT |
| Test Result | ✅ API WORKING |
| Buy Threshold | $0.00000600 |
| Sell Target | $0.00000720 (+20%) |
| Position Size | $5.00/trade |
| USDT Balance | $13.73 |

### Daily Scalping Bot
| Setting | Value |
|---------|-------|
| File | daily_scalper.py |
| Profit Target | +5% |
| Schedule | 8 AM, 2 PM, 8 PM |
| Max Daily | 5 trades / $5 |

### Bot Rename
- **Name:** 🐕 Trading Bot
- **Username:** @pepew_alert_bot

## PEPEW Trading Bot ⭐ CRITICAL

### ⚠️ API STATUS: NONKYC API BROKEN
All API keys returning HTML/302 redirect instead of JSON.
Auto-fix system created - monitors and alerts when fixed.

### Quick Commands
```bash
# Check API status
python3 /Users/maxwell/.openclaw/workspace/trading_bot/api_monitor.py

# Run bot
cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 trading_bot.py

# View logs
tail -f data/trading_bot.log
```

### Cron Jobs (Active)
| Job | Schedule |
|-----|----------|
| Morning Scalper | 8:00 AM |
| Mid-Day Review | 2:00 PM |
| Evening Review | 6:00 PM |
| Trading Check | Every 4 hours |

### Portfolio
| Metric | Value |
|--------|-------|
| PEPEW Balance | 46,105,088 PEPEW |
| PEPEW Value | ~$19.73 |
| Masternode | P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj |
| Explorer | https://explorer.pepepow.org/address/P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj |
| Website | https://pepepow.org/ |

### Historical Performance
- Starting (Jan 28): $16.14
- Current (Feb 03): $19.73
- Gain: +$3.60 (+22.29%)

## Additional Notes

### Moltbook (Inactive)
- Profile: https://www.moltbook.com/u/Lassie
- API registration expired
- Skill installed but not functional
- Re-registration needed on different network

### Python Course
- All 14 lessons completed
- Saved to `/Users/maxwell/.openclaw/workspace/lessons/`
- Bonus lessons: API calls, Telegram alerts, web scraping, pandas

### PEPEW Fetcher
- Uses Playwright-stealth to bypass bot detection
- Command: `python3 /Users/maxwell/.openclaw/workspace/trading_bot/pepew_price.py`

### Model Question
- GLM 4.7 doesn't cause memory loss
- Memory stored in files, not model context

## Key Dates
- **2026-01-28:** Portfolio tracking started ($16.14)
- **2026-02-03:** First OpenClaw session + memory recovery
- **2026-02-04:** Auto-systems day (backup, fix, skills)

## Auto-Systems Created

### Auto-Fix System
Location: `/Users/maxwell/.openclaw/workspace/auto-fix/`
- Detects problems automatically
- Alerts BEFORE fixing (asks approval)
- Learns from solved issues

### Backup System
Location: `/Users/maxwell/.openclaw/workspace/backup.py`
- Manual: `python3 /Users/maxell/.openclaw/workspace/backup.py`
- Auto: Daily at 3 AM via LaunchAgent
- Location: `~/Desktop/OpenClaw-Backup/`
- Keeps: Last 7 daily backups

### Skills Installed
- `/crypto` - Price, portfolio, alerts
- `/news` - Crypto news from RSS feeds
- `/problems` - Learn and solve issues

## Daily Reminders
- **7:57 AM** - Snack time 🍎
