# Cron Jobs Persistence Research for macOS

**Research Date:** February 4, 2026  
**Purpose:** Ensure trading bot runs persistently on macOS

---

## Why Cron Jobs Fail on macOS

### 1. Cron Daemon Not Running by Default

**Problem:** Unlike Linux, macOS does **not** automatically start the cron daemon on boot. The cron binary exists at `/usr/sbin/cron` but is not enabled by default.

**Symptoms:**
- `crontab -l` shows entries but they never run
- No cron process in `ps aux | grep cron`
- `launchctl list | grep cron` shows nothing

**macOS Behavior:**
- macOS has deprecated cron in favor of `launchd`
- cron is still available but not automatically started
- Requires manual enabling or installation

### 2. System Integrity Protection (SIP) Issues

**Problem:** macOS System Integrity Protection (SIP) can interfere with cron in several ways:
- Prevents cron from accessing certain system directories
- May block cron from sending emails or using certain APIs
- Full disk access permissions required

**Solution:**
- Grant "Full Disk Access" to Terminal or cron in System Preferences > Security & Privacy > Privacy
- For cron specifically, add to allowed apps if needed

### 3. Permissions Problems

**Common Permission Issues:**
- User's crontab file has wrong permissions (should be 600)
- Script files in cron jobs need executable permissions
- Working directory access issues

**Fix:**
```bash
# Fix crontab permissions
chmod 600 ~/.crontab

# Fix script permissions
chmod +x /path/to/script.sh

# Ensure user has cron access
sudo chown root:wheel /usr/sbin/cron  # if needed
```

### 4. Environment Variables

**Problem:** Cron jobs run in a minimal environment:
- No PATH by default
- No shell profile loaded
- Different HOME directory

**Solution:** Always use full paths in cron jobs:
```bash
# BAD
0 6 * * * python3 trading_bot.py

# GOOD
0 6 * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && /usr/bin/python3 trading_bot.py >> /tmp/trading_bot.log 2>&1
```

---

## How to Enable and Start Cron Daemon on macOS

### Method 1: Manual Start (Temporary)

```bash
# Start cron daemon
sudo cron start

# Verify it's running
ps aux | grep cron

# Stop cron daemon
sudo cron stop
```

### Method 2: Auto-Start on Boot (Recommended)

```bash
# Create launchd plist for cron
sudo nano /System/Library/LaunchDaemons/com.apple.cron.plist

# With content:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.apple.cron</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/sbin/cron</string>
    </array>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>

# Load the plist
sudo launchctl load /System/Library/LaunchDaemons/com.apple.cron.plist

# Enable auto-start
sudo launchctl enable system/com.apple.cron
```

### Method 3: Homebrew Cron (Alternative)

```bash
# Install cron via Homebrew (includes launchd integration)
brew install cron

# Homebrew automatically sets up launchd plist
brew services start cron
```

---

## Alternative: launchd/launchctl (Preferred on macOS)

### Why launchd is Better

1. **Native to macOS** - Apple's official process manager
2. **Auto-restart** - Built-in KeepAlive support
3. **Dependency management** - Can depend on network, other services
4. **Logging** - Integrated with macOS logging system
5. **Security** - Better integration with macOS security features

### Launchd Concepts

- **Daemons** - System-wide services (run as root)
- **Agents** - User-specific services (run as user)
- **Label** - Unique identifier for the service
- **ProgramArguments** - Command and arguments
- **RunAtLoad** - Start when loaded
- **KeepAlive** - Restart if crashes
- **StartInterval** - Run every N seconds
- **StartCalendarInterval** - Run at specific times (like cron)

### Launchd Plist for Trading Bot

**Location:** `~/Library/LaunchAgents/` (for user agents)

**Example plist (already created at `/Users/maxwell/.openclaw/workspace/trading_bot/trading-bot.plist`):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>ai.openclaw.trading-bot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/maxwell/.openclaw/workspace/trading_bot/trading_bot.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/maxwell/.openclaw/workspace/trading_bot</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/openclaw-trading-bot.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/openclaw-trading-bot.error.log</string>
    <key>StartInterval</key>
    <integer>3600</integer>
</dict>
</plist>
```

### Managing the Trading Bot Service

```bash
# Install the plist to LaunchAgents
cp /Users/maxwell/.openclaw/workspace/trading_bot/trading-bot.plist ~/Library/LaunchAgents/

# Load and start the service
launchctl load ~/Library/LaunchAgents/trading-bot.plist
launchctl start ai.openclaw.trading-bot

# Check status
launchctl list | grep trading-bot

# View logs
tail -f /tmp/openclaw-trading-bot.log
tail -f /tmp/openclaw-trading-bot.error.log

# Stop the service
launchctl stop ai.openclaw.trading-bot
launchctl unload ~/Library/LaunchAgents/trading-bot.plist

# Restart the service
launchctl unload ~/Library/LaunchAgents/trading-bot.plist
launchctl load ~/Library/LaunchAgents/trading-bot.plist
```

---

## Debugging Cron Job Failures

### Debugging Cron Issues

```bash
# Check if cron is running
ps aux | grep cron

# Check cron logs
sudo grep cron /var/log/system.log
log show --predicate 'eventMessage CONTAINS "cron"' --last 1h

# Test cron environment
crontab -e
# Add test entry:
# * * * * * env > /tmp/cron_env.txt
# Check the output file
cat /tmp/cron_env.txt
```

### Debugging Launchd Issues

```bash
# Check service status
launchctl list | grep trading-bot

# Check for errors
launchctl error ai.openclaw.trading-bot

# View detailed logs
log show --predicate 'processImagePath CONTAINS "trading_bot"' --last 1h

# Check stderr/stdout files
cat /tmp/openclaw-trading-bot.error.log
cat /tmp/openclaw-trading-bot.log

# Debug with Console app
# Open Console app and search for "trading-bot" or "openclaw"
```

### Common Debugging Steps

1. **Check if script runs manually first**
   ```bash
   cd /Users/maxwell/.openclaw/workspace/trading_bot
   /usr/bin/python3 trading_bot.py
   ```

2. **Verify paths and permissions**
   ```bash
   ls -la /Users/maxwell/.openclaw/workspace/trading_bot/
   file /usr/bin/python3
   ```

3. **Test in isolated environment**
   ```bash
   env -i PATH=/usr/bin:/bin /usr/bin/python3 /Users/maxwell/.openclaw/workspace/trading_bot/trading_bot.py
   ```

4. **Check dependencies**
   ```bash
   # Python dependencies
   pip3 list | grep -E "(requests|websockets)"

   # Network connectivity
   curl -I https://api.example.com
   ```

---

## Best Practices for Persistent Scheduled Tasks on macOS

### 1. Use Launchd Instead of Cron

**Recommendation:** For new projects, use launchd from the start.

**Benefits:**
- Native macOS integration
- Automatic restart on crash
- Better logging
- Dependency handling

### 2. Proper Error Handling

```python
# In trading_bot.py - add robust error handling
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/trading_bot.log'),
        logging.StreamHandler()
    ]
)

try:
    main()
except Exception as e:
    logging.error(f"Critical error: {e}")
    sys.exit(1)
```

### 3. Logging Best Practices

```xml
<!-- In launchd plist -->
<key>StandardOutPath</key>
<string>/tmp/openclaw-trading-bot.log</string>
<key>StandardErrorPath</key>
<string>/tmp/openclaw-trading-bot.error.log</key>
<key>EnvironmentVariables</key>
<dict>
    <key>PYTHONPATH</key>
    <string>/Users/maxwell/.openclaw/workspace/trading_bot</string>
    <key>LOG_LEVEL</key>
    <string>INFO</string>
</dict>
```

### 4. Monitoring and Alerts

```python
# Add health check endpoint or monitoring
import os

def health_check():
    if not os.path.exists('/tmp/trading_bot.lock'):
        return False, "Lock file missing"
    
    # Check last activity
    stat = os.stat('/tmp/trading_bot.log')
    if time.time() - stat.st_mtime > 7200:  # 2 hours
        return False, "No activity in 2 hours"
    
    return True, "OK"
```

### 5. Resource Limits

```xml
<!-- Add to launchd plist for resource management -->
<key>HardResourceLimits</key>
<dict>
    <key>NumberOfFiles</key>
    <integer>1024</integer>
</dict>
<key>SoftResourceLimits</key>
<dict>
    <key>NumberOfFiles</key>
    <integer>1024</integer>
</dict>
```

---

## Final Working Solution for Maxwell's Trading Bot

### Current Setup

✅ **Launchd plist already created at:**
```
/Users/maxwell/.openclaw/workspace/trading_bot/trading-bot.plist
```

**Configuration:**
- Label: `ai.openclaw.trading-bot`
- Program: `/usr/bin/python3` with `/Users/maxwell/.openclaw/workspace/trading_bot/trading_bot.py`
- Working Directory: `/Users/maxwell/.openclaw/workspace/trading_bot`
- RunAtLoad: `true`
- KeepAlive: `true`
- StartInterval: `3600` (1 hour)
- Logs: `/tmp/openclaw-trading-bot.log` and `/tmp/openclaw-trading-bot.error.log`

### Installation Steps

```bash
# 1. Copy plist to LaunchAgents
cp /Users/maxwell/.openclaw/workspace/trading_bot/trading-bot.plist ~/Library/LaunchAgents/

# 2. Set correct permissions
chmod 644 ~/Library/LaunchAgents/trading-bot.plist

# 3. Load and start
launchctl load ~/Library/LaunchAgents/trading-bot.plist
launchctl start ai.openclaw.trading-bot

# 4. Verify it's running
launchctl list | grep trading-bot
ps aux | grep trading_bot

# 5. Check logs
tail -f /tmp/openclaw-trading-bot.log
```

### If cron is Still Needed as Backup

```bash
# Enable cron daemon
sudo cron start

# Add cron entry as backup
crontab -e
# Add:
# 0 * * * * cd /Users/maxwell/.openclaw/workspace/trading_bot && /usr/bin/python3 trading_bot.py >> /tmp/trading_bot_cron.log 2>&1
```

### Verification Commands

```bash
# Check service status
echo "=== Launchd Status ==="
launchctl list | grep trading-bot

# Check process
echo "=== Process ==="
ps aux | grep trading_bot | grep -v grep

# Check logs
echo "=== Recent Logs ==="
tail -20 /tmp/openclaw-trading-bot.log

# Check errors
echo "=== Errors ==="
tail -20 /tmp/openclaw-trading-bot.error.log
```

### Troubleshooting Quick Reference

| Issue | Solution |
|-------|----------|
| Service won't start | Check logs: `tail /tmp/openclaw-trading-bot.error.log` |
| Service crashes immediately | Run manually: `cd /Users/maxwell/.openclaw/workspace/trading_bot && /usr/bin/python3 trading_bot.py` |
| Service not running after reboot | Verify plist in `~/Library/LaunchAgents/` and loaded |
| No output in logs | Check Python script runs without errors |
| Permission denied | `chmod +x` on script, check file ownership |

---

## Summary

**Key Findings:**
1. Cron daemon is **not running by default** on modern macOS
2. **launchd is the preferred method** for persistent services on macOS
3. Maxwell already has a **well-configured launchd plist** for the trading bot
4. The solution uses `KeepAlive=true` to automatically restart on crash
5. `StartInterval=3600` runs the bot every hour

**Recommended Action:**
1. Copy the existing plist to `~/Library/LaunchAgents/`
2. Load with `launchctl load`
3. Verify with `launchctl list` and log inspection

This setup provides robust, persistent operation suitable for a trading bot that needs to run continuously.
