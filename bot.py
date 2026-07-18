import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("🚀 Initializing cloud-hosted Chrome application...")

# 1. Define Chrome Options correctly before using them
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Point Chrome to our background display server
os.environ["DISPLAY"] = ":1"

# 2. Start the browser engine safely
driver = webdriver.Chrome(options=options)

try:
    # Set standard desktop window dimensions
    driver.set_window_size(1280, 800)
    
    print("📡 >>> Connecting to network interface...")
    driver.get("https://www.google.com")
    
    # Handle Google's cloud cookie consent overlay if it shows up
    try:
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Accept all") or contains(., "I agree")]'))
        )
        cookie_btn.click()
        print("🍪 >>> Handled cookie consent overlay.")
    except Exception:
        pass

    print("🔍 >>> Target locked. Finding text input layouts...")
    
    # Wait until the search box is completely loaded and clickable
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    
    print("⌨️ >>> Injecting search sequences dynamically...")
    search_box.click()
    search_box.send_keys("Python automation workflows")
    search_box.send_keys(Keys.RETURN)
    
    print("✅ >>> Render complete! Keeping browser alive...")
    time.sleep(400)

except Exception as e:
    print(f"❌ >>> Session aborted due to configuration error: {e}")
finally:
    driver.quit()
    print("🔒 >>> Cloud automation cycle closed successfully.")
    
