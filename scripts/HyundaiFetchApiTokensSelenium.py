#!/usr/bin/env python3
"""
Hyundai EU Refresh Token Extractor
Uses the Hyundai CTB (Connected to Bluelink) endpoint which doesn't have WAF blocking
Based on: https://gist.github.com/chrisf4lc0n/d5506bd69e0d07b53574442c972090fe

Requirements:
- Google Chrome browser (will auto-install via Homebrew if not found)
- Python packages: selenium, requests
"""

import re
import time
import os
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

# Hyundai EU OAuth2 Configuration (CTB endpoint - no WAF!)
#
# REQUIRED: You must obtain Hyundai's OAuth2 client credentials before running this script.
# These are Hyundai's official OAuth2 client credentials from their mobile app (not personal credentials).
#
# To obtain these credentials:
# 1. Search online for "Hyundai Bluelink OAuth2 client credentials" or check the Hyundai/Kia Connect integration documentation
# 2. Look for CLIENT_ID and CLIENT_SECRET values used by the mobile app
# 3. Fill them in below before running the script
#
# Your personal authentication happens via browser login, and the refresh token generated is YOUR secret.
# Never share your refresh token - it provides full access to your vehicle account.
#
CLIENT_ID = ""  # TODO: Fill in Hyundai OAuth2 CLIENT_ID here
CLIENT_SECRET = ""  # TODO: Fill in Hyundai OAuth2 CLIENT_SECRET here
BASE_URL = "https://idpconnect-eu.hyundai.com/auth/api/v2/user/oauth2/"

# Mobile user agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 4.1.1; Galaxy Nexus Build/JRO03C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19_CCS_APP_AOS"

def check_homebrew():
    """Check if Homebrew is installed"""
    try:
        subprocess.run(['brew', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_chrome():
    """Install Google Chrome via Homebrew"""
    if not check_homebrew():
        print("❌ Homebrew not found. Please install Homebrew first:")
        print("   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        return False

    print("📦 Installing Google Chrome via Homebrew...")
    try:
        subprocess.run(['brew', 'install', '--cask', 'google-chrome'], check=True)
        print("✅ Google Chrome installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Google Chrome")
        return False

def find_chrome():
    """Find Chrome executable, install if not found"""
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    if os.path.exists(chrome_path):
        return chrome_path

    print("⚠️  Google Chrome not found")
    response = input("Would you like to install it via Homebrew? (y/n): ").strip().lower()

    if response == 'y':
        if install_chrome():
            if os.path.exists(chrome_path):
                return chrome_path

    print("❌ Google Chrome is required to run this script")
    print("   Please install it manually from: https://www.google.com/chrome/")
    return None

def setup_driver():
    """Setup Chrome driver with mobile user agent"""
    chrome_path = find_chrome()
    if not chrome_path:
        return None

    options = Options()
    options.add_argument(f"user-agent={MOBILE_USER_AGENT}")
    options.binary_location = chrome_path
    options.add_argument("--window-size=800,600")
    options.add_argument("--window-position=0,0")
    # Use a separate user data directory to avoid conflicts
    options.add_argument("--user-data-dir=/tmp/selenium-chrome-hyundai")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"⚠️  ChromeDriver not found, installing automatically...")
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
            return driver
        except Exception as e2:
            print(f"❌ Error setting up ChromeDriver: {e2}")
            print("   Try: pip install webdriver-manager")
            return None

def main():
    print("="*60)
    print("Hyundai EU Refresh Token Extractor")
    print("="*60)

    # Validate credentials are filled in
    if not CLIENT_ID or not CLIENT_SECRET:
        print("\n❌ ERROR: CLIENT_ID and CLIENT_SECRET must be filled in!")
        print("\nPlease edit this script and add Hyundai's OAuth2 credentials:")
        print("  1. Search online for 'Hyundai Bluelink OAuth2 client credentials'")
        print("  2. Fill in CLIENT_ID and CLIENT_SECRET at the top of this file")
        print("  3. These are Hyundai's public app credentials (not your personal credentials)")
        print("\nYour personal authentication happens via browser login.")
        return

    driver = setup_driver()
    if not driver:
        return

    try:
        # Step 1: Open login page (CTB endpoint - no WAF!)
        login_url = (
            f"{BASE_URL}authorize?"
            f"client_id=peuhyundaiidm-ctb&"
            f"redirect_uri=https%3A%2F%2Fctbapi.hyundai-europe.com%2Fapi%2Fauth&"
            f"nonce=&state=PL_&"
            f"scope=openid+profile+email+phone&"
            f"response_type=code&"
            f"connector_client_id=peuhyundaiidm-ctb&"
            f"connector_scope=&"
            f"connector_session_key=&"
            f"country=&"
            f"captcha=1&"
            f"ui_locales=en-US"
        )

        print("\n🌐 Opening Hyundai login page in browser...")
        print("="*60)
        print("📝 PLEASE COMPLETE THE FOLLOWING STEPS:")
        print("   1. Log in with your Hyundai BlueLink email and password")
        print("   2. Solve the reCAPTCHA if prompted")
        print("   3. Complete the login process")
        print("="*60)

        driver.get(login_url)

        input("\n⏸️  Press ENTER after you have successfully logged in...")

        # Step 2: Get authorization code
        print("\n🔄 Getting authorization code...")
        auth_url = (
            f"{BASE_URL}authorize?"
            f"response_type=code&"
            f"client_id={CLIENT_ID}&"
            f"redirect_uri=https://prd.eu-ccapi.hyundai.com:8080/api/v1/user/oauth2/token&"
            f"lang=de&"
            f"state=ccsp"
        )

        driver.get(auth_url)
        time.sleep(2)

        # Extract code from URL
        current_url = driver.current_url
        code_match = re.search(r'code=([^&]+)', current_url)

        if not code_match:
            print("\n❌ Error: Could not find authorization code in URL")
            print(f"Current URL: {current_url}")
            return

        auth_code = code_match.group(1)
        print(f"✓ Authorization code obtained: {auth_code[:20]}...")

        # Step 3: Exchange code for refresh token
        print("\n🔄 Exchanging code for refresh token...")

        token_data = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": "https://prd.eu-ccapi.hyundai.com:8080/api/v1/user/oauth2/token",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }

        response = requests.post(f"{BASE_URL}token", data=token_data)

        if response.status_code == 200:
            tokens = response.json()
            refresh_token = tokens.get("refresh_token")

            if refresh_token:
                print("\n" + "="*60)
                print("✅ SUCCESS! Your Hyundai EU Refresh Token:")
                print("="*60)
                print(f"\n{refresh_token}\n")
                print("="*60)
                print("\n📋 NEXT STEPS:")
                print("   1. Copy the token above")
                print("   2. In Home Assistant, go to Settings → Integrations")
                print("   3. Add 'Hyundai / Kia Connect' integration")
                print("   4. Select Region: EU, Brand: Hyundai")
                print("   5. Enter your email as Username")
                print("   6. Paste the token as Password")
                print("   7. Enter your vehicle PIN")
                print("\n⏰ Token is valid for 180 days")
                print("="*60)
            else:
                print("\n❌ Error: No refresh token in response")
                print(f"Response: {tokens}")
        else:
            print(f"\n❌ Error exchanging code for token: {response.status_code}")
            print(f"Response: {response.text}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n🔒 Closing browser...")
        driver.quit()

if __name__ == "__main__":
    main()
