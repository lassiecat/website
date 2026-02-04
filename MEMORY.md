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

### API Status: WORKING (Feb 4)
- NonKYC API v2 migrated - new keys required
- Basic Auth works: `api_key` + `api_secret` base64 encoded
- New keys: `fd2199b9e480ae4e6448192f4481e847` / `0251ccfa65d229f273fe9862d0847bfac9efdff7aa5f6fba`

### Bot Location
```
/Users/maxwell/.openclaw/workspace/trading_bot/
├── quick_trader.py       # SHIB quick profit trader
├── pepew_trader.py      # PEPEW quick profit trader
├── api_monitor.py       # API status monitor
├── config.py            # API KEYS HERE
├── nonkyc_v2.py        # NonKYC v2 API client
├── telegram_alerts.py   # Telegram notifications
└── data/
    ├── price_history.csv
    └── trades.json
```

### SHIB Trading Strategy (Quick Profits)
| Setting | Value |
|---------|-------|
| Buy Amount | $1.10 per trade |
| Sell Targets | +2%, +3%, +5% |
| Fees | 0.3% (buy 0.2% + sell 0.1%) |
| Net Profit | ~1.7% to 4.7% |
| Status | Active |

### PEPEW Trading Strategy (Quick Profits)
| Setting | Value |
|---------|-------|
| Buy Amount | $1.00 per trade |
| Sell Targets | +2%, +3%, +5% |
| Min Order | 200,000 PEPEW |
| Status | Active |

### API Credentials (Latest - Feb 4)
```python
NONKYC = {
    "api_key": "fd2199b9e480ae4e6448192f4481e847",
    "api_secret": "0251ccfa65d229f273fe9862d0847bfac9efdff7aa5f6fba",
    "base_url": "https://api.nonkyc.io/api/v2",
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
- **7:57 AM** - Snack time 🍎 (tested, disabled)

## Auto-Systems

### Backup System
- Manual: `python3 /Users/maxwell/.openclaw/workspace/backup.py`
- Auto: Daily at 3 AM via LaunchAgent
- Location: `~/Desktop/OpenClaw-Backup/`
- Keeps: Last 7 daily backups

### Auto-Fix System
- `/Users/maxwell/.openclaw/workspace/auto-fix/detect_alert.py`
- Monitors for issues
- Alerts before fixing

### Skills Installed
- `/crypto` - Price, portfolio, alerts
- `/news` - Crypto news from RSS feeds
- `/problems` - Learn and solve issues

## Crypto Watchlist

| Coin | Symbol | Price | Notes |
|------|--------|-------|-------|
| Hedera | HBAR | $0.093 | Enterprise L1, Google/IBM backing |
| Shiba Inu | SHIB | $0.00000677 | Quick profit trading |
| PEPEW | PEPEW | $0.00000042 | Quick profit trading |

### Hedera (HBAR) - Added Feb 4
- Price: $0.0928
- Market Cap: ~$4B
- Rank: #30
- Enterprise governance (Google, IBM, Boeing)
- Watchlist file: `/Users/maxwell/.openclaw/workspace/crypto_watchlist.md`
