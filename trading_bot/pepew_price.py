#!/usr/bin/env python3
"""
PEPEW Price Fetcher with Playwright Stealth
Bypasses bot detection on NonKYC and PEPEW Explorer
"""

import asyncio
from playwright.async_api import async_playwright
import json

async def get_pepew_price():
    """Get PEPEW price using Playwright with stealth mode"""
    
    async with async_playwright() as p:
        # Launch browser with stealth settings
        browser = await p.chromium.launch(headless=True)
        
        # Create stealth context
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            locale='en-US',
        )
        
        # Add stealth plugin to evade detection
        page = await context.new_page()
        
        # Stealth settings - evades bot detection
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
            window.chrome = {
                runtime: {},
                loadTimes: () => {},
                csi: () => {},
            };
            Object.defineProperty(window, 'innerWidth', {
                get: () => 1920
            });
            Object.defineProperty(window, 'innerHeight', {
                get: () => 1080
            });
            Object.defineProperty(document, 'hidden', {
                get: () => false
            });
            navigator.permissions.query = {then: (cb) => cb({state: 'granted'})};
        """)
        
        results = {
            'pepew_price': None,
            'balance': None,
            'errors': []
        }
        
        # Get PEPEW price from NonKYC
        try:
            print("🌐 Fetching PEPEW price from NonKYC...")
            await page.goto('https://nonkyc.io/market/PEPEW_USDT', wait_until='networkidle', timeout=30000)
            
            # Wait for price to load
            await page.wait_for_timeout(3000)
            
            # Try to find price element
            try:
                price_element = await page.query_selector('.price, .ticker-price, [class*="price"]')
                if price_element:
                    price_text = await price_element.text_content()
                    if price_text:
                        # Clean up price
                        price = float(price_text.replace('$', '').replace(',', ''))
                        results['pepew_price'] = price
                        print(f"✅ PEPEW Price: ${price}")
            except Exception as e:
                results['errors'].append(f"NonKYC price: {e}")
                print(f"⚠️ Could not find price on NonKYC")
        except Exception as e:
            results['errors'].append(f"NonKYC page: {e}")
            print(f"❌ NonKYC error: {e}")
        
        # Get balance from PEPEW Explorer
        try:
            print("🌐 Fetching balance from PEPEW Explorer...")
            await page.goto('https://explorer.pepepow.org/address/P914pwEXrECewzQED9MR9X1vjTnaXXt7Wj', wait_until='networkidle', timeout=30000)
            
            # Wait for balance to load
            await page.wait_for_timeout(3000)
            
            # Try to find balance element
            try:
                balance_element = await page.query_selector('.balance, .amount, [class*="balance"]')
                if balance_element:
                    balance_text = await balance_element.text_content()
                    if balance_text:
                        # Clean up balance - extract number
                        import re
                        numbers = re.findall(r'[\d,]+\.?\d*', balance_text.replace(',', ''))
                        if numbers:
                            balance = int(float(numbers[0].replace(',', '')))
                            results['balance'] = balance
                            print(f"✅ PEPEW Balance: {balance:,}")
            except Exception as e:
                results['errors'].append(f"Explorer balance: {e}")
                print(f"⚠️ Could not find balance on Explorer")
        except Exception as e:
            results['errors'].append(f"Explorer page: {e}")
            print(f"❌ Explorer error: {e}")
        
        await browser.close()
        
        return results

def main():
    """Main function"""
    print("\n🐕 PEPEW LIVE DATA")
    print("="*50)
    
    results = asyncio.run(get_pepew_price())
    
    print("\n" + "="*50)
    print("RESULTS:")
    if results['pepew_price']:
        print(f"  Price (NonKYC): ${results['pepew_price']}")
    if results['balance']:
        print(f"  Balance (Explorer): {results['balance']:,} PEPEW")
    
    if results['errors']:
        print(f"\n⚠️ Errors encountered:")
        for error in results['errors']:
            print(f"  - {error}")
    
    print("="*50 + "\n")

if __name__ == '__main__':
    main()
