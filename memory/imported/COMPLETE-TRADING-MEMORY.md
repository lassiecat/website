# Complete Trading Bot Memory - Consolidated

**Last Updated:** 2026-02-03
**Source:** Telegram chat history PDFs (1.pdf, a.pdf, b.pdf, c.pdf, d.pdf)

---

## Bot Overview

**Name:** 🐕 Trading Bot
**Username:** @pepew_alert_bot
**Location:** `/Users/maxwell/.openclaw/workspace/trading_bot/`

---

## Files Created

```
trading_bot/
├── trading_bot.py       # Main trading bot
├── price_fetcher.py     # Live price fetching
├── config.py           # API keys & settings
├── auto_trader.py      # Auto-adjusts strategy daily
├── daily_scalper.py    # Quick +5% profit trades
├── browser_trader.py   # Browser automation (2FA blocked)
├── pepew_price.py      # PEPEW price fetcher (Playwright-stealth)
└── data/
    ├── price_history.csv
    ├── alerts.log
    └── trading_bot.log
```

---

## API Credentials

### NonKYC Exchange
```python
NONKYC = {
    "api_key": "c677d4108806428c97a89a0e31597029",
    "api_secret": "7bd6623182d9b7f96eee360cb1d12b700941cb7b",
    "enabled": True
}
```
- Dashboard: https://nonkyc.io
- PEPEW Market: https://nonkyc.io/market/PEPEW_USDT
- SHIB Market: https://nonkyc.io/market/SHIB_USDT

### Telegram Alerts
```python
TELEGRAM = {
    "bot_token": "8396730713:AAETb_miSVW7H_rUlk4Fl_p-Q06WuKrm-2Y",
    "chat_id": "6404339546",
    "enabled": True
}
```

---

## Critical: NonKYC API Limitation

### PEPEW API Blocked
```json
{
  "symbol": "PEPEW/USDT",
  "apiExcluded": true  // TRADING VIA API DISABLED!
}
```

**Problem:** NonKYC blocks API trading for PEPEW — only website trading allowed.
**Impact:** Orders placed via API won't execute.
**Workaround:** Switched to SHIB/USDT for live API trading.

---

## SHIB/USDT Live Trading

### Test Results (API Confirmed Working!)
| Metric | Value |
|--------|-------|
| Symbol | SHIB/USDT |
| Price Tested | $0.00000653 |
| Order Test | ✅ Success |
| Status | 🔴 LIVE TRADING |

### Configuration
```python
SHIB_USDT = {
    "symbol": "SHIB/USDT",
    "buy_threshold": 0.00000600,
    "sell_target": 0.00000720,  # +20%
    "position_size": 1.50,
    "max_daily": 5.00,
    "usdt_balance": 13.73
}
```

### High Volume Alternatives (API-Enabled)
| Symbol | Price | 24h Volume |
|--------|-------|------------|
| ETH/USDT | $2,134.35 | $13.9M |
| BTC/USDT | $74,202.38 | $13.7M |
| SHIB/USDT | $0.00000654 | $353K |
| ARRR/USDT | $0.38 | $280K |
| TRX/USDT | $0.28 | $159K |

### Cheap Low-Volume Alternatives
| Symbol | Price |
|--------|-------|
| DOGS/USDT | $0.000000007 |
| PHIL/USDT | $0.00000000005935 |
| DFAT/USDT | $0.0000000508 |

---

## Trading Strategies

### Strategy 1: Main Trading Bot
| Setting | Value |
|---------|-------|
| Mode | 🔴 LIVE |
| Daily Limit | $5.00 |
| Position | $5/trade |
| Buy | < $0.0000003843 |
| Sell | > $0.0000005124 (+30%) |
| Stop Loss | -10% |
| Take Profit | +20% |

### Strategy 2: Daily Scalper (+5% profits)
| Setting | Value |
|---------|-------|
| File | daily_scalper.py |
| Profit Target | +5% |
| Schedule | 8 AM, 2 PM, 8 PM |
| Max Daily | 5 trades / $5 |

---

## Auto-Trading System

### Cron Jobs Active
| Time | Action |
|------|--------|
| 8:00 AM | Auto-adjust strategy |
| 2:00 PM | Mid-day review |
| 6:00 PM | Evening review |
| Every 4 hours | Trading check |

### Commands
```bash
# Run bot
cd /Users/maxwell/.openclaw/workspace/trading_bot
python3 trading_bot.py              # Continuous
python3 trading_bot.py --once       # Single check
python3 trading_bot.py --stats      # Statistics
python3 daily_scalper.py            # Quick scalp

# View logs
tail -f trading_bot.log
cat data/price_history.csv
```

---

## Portfolio

### PEPEW Holdings
| Metric | Value |
|--------|-------|
| Balance | 46,105,088 PEPEW |
| Value | ~$19.73 |
| Masternode | P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj |
| Explorer | https://explorer.pepepow.org/address/P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj |
| Website | https://pepepow.org/ |

### SHIB Trading Balance
- USDT: $13.73

### Historical Performance
| Date | Value | Change |
|------|-------|--------|
| Jan 28 | $16.14 | - |
| Feb 03 | $19.73 | +$3.60 (+22.29%) |

---

## Python Lessons Completed

**All 14 Lessons Saved:** `/Users/maxwell/.openclaw/workspace/lessons/`

### Basic Course
1. Variables, Data Types, Print
2. Lists & Loops
3. If/Else Statements
4. Functions
5. Dictionaries
6. File I/O
7. Error Handling
8. Modules & Imports
9. Price Alert Bot (Full Project!)

### Bonus Course
11. Real API Calls (requests library)
12. Telegram Alerts (Bot API)
13. Web Scraping (BeautifulSoup)
14. Pandas for Data Analysis

---

## Moltbook Integration

### Profile
- **URL:** https://www.moltbook.com/u/Lassie
- **Status:** Inactive (API key expired)

### Credentials (expired)
```json
{
  "api_key": "moltsky-...",
  "agent_name": "Lassie"
}
```

### Re-registration Required
```bash
curl -X POST https://www.moltbook.com/api/v1/agents/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Lassie", "description": "Digital companion"}'
```

---

## PEPEW Price Fetcher

**Fix:** Playwright-stealth bypasses bot detection

**Usage:**
```bash
python3 /Users/maxwell/.openclaw/workspace/pepew_price.py
```

**Sample Output:**
```
🐕 PEPEW LIVE DATA
Price: $0.000000428
Balance: 46105088 PEPEW (est.)
```

---

## Reminders Set

- ⏰ 3:15am - Coding session wake-up
- ⏰ 4:35am - L-Arginine reminder

---

## Notes

- Cron jobs not persisting (issue investigated)
- Model switches don't affect memory files
- All files stored in `/Users/maxwell/.openclaw/workspace/`
