# Trading Bot Addendum - SHIB/USDT & Daily Scalper

## Critical NonKYC API Finding

### PEPEW API Blocked
```json
{
  "symbol": "PEPEW/USDT",
  "apiExcluded": true  // API TRADING DISABLED!
}
```

NonKYC has **disabled API trading for PEPEW** specifically. This is why earlier orders weren't going through.

**Solutions Explored:**
1. Browser automation (blocked by 2FA)
2. Switch to another exchange (MEXC, Bitget)
3. Trade a different coin with API support

**Chosen Solution:** Trade SHIB/USDT via API (fully supported!)

---

## SHIB/USDT Live Trading

### Test Results (Confirmed Working!)
| Metric | Value |
|--------|-------|
| Symbol | SHIB/USDT |
| Price Tested | $0.00000653 |
| Order Type | Limit buy |
| Amount | 229,709 SHIB ($1.50) |
| Status | ✅ API Working |

### SHIB Trading Configuration
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

### Cheap Alternatives (Low Volume)
| Symbol | Price |
|--------|-------|
| DOGS/USDT | $0.000000007 |
| PHIL/USDT | $0.00000000005935 |
| DFAT/USDT | $0.0000000508 |
| TTC/USDT | $0.00000406 |

---

## Daily Scalping Bot

### Created: `daily_scalper.py`
Quick profit strategy for frequent small gains.

### Strategy
| Setting | Value |
|---------|-------|
| Profit Target | +5% |
| Stop Loss | -10% |
| Position | $1-1.50/trade |
| Max Daily | 5 trades / $5 |
| Schedule | 8 AM, 2 PM, 8 PM |

### Cron Jobs
```bash
# Morning scalp check
0 8 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 daily_scalper.py

# Afternoon monitoring
0 14 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 daily_scalper.py

# Evening profit check
0 20 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && python3 daily_scalper.py
```

### Files Created
- `daily_scalper.py` - Quick profit scalping bot
- Updated README.md with scalping strategy

---

## Bot Rename

### Telegram Bot
- **Old Name:** PEPEW Alert Bot
- **New Name:** 🐕 Trading Bot
- **Username:** @pepew_alert_bot (unchanged)

### Files Updated
- trading_bot.py
- auto_trader.py
- daily_scalper.py
- README.md
- TELEGRAM_SETUP.md
- config.py

---

## Key Findings Summary

### What Works
✅ NonKYC API for public data (prices, orderbook)
✅ SHIB/USDT trading via API
✅ Place orders, cancel orders, get balances
✅ Telegram alerts

### What Doesn't Work
❌ PEPEW/USDT via API (apiExcluded: true)
❌ Browser automation with 2FA enabled

### Recommendations
1. Use SHIB/USDT for live API trading
2. Keep PEPEW for masternodes (not trading)
3. Alternative: Switch to MEXC for full PEPEW API support

---

## Notes
- All bot files in `/Users/maxwell/.openclaw/workspace/trading_bot/`
- Daily scalper designed for quick +5% profits
- Max 5 trades/day, $5 volume limit
- Telegram bot name changed to 🐕 Trading Bot
