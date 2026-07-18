from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ... (your existing chrome options setup above) ...

driver = webdriver.Chrome(options=options)

try:
    # 1. Force the browser layout to expand completely
    driver.set_window_size(1280, 800)
    
    print("📡 >>> Connecting to network interface...")
    driver.get("https://www.google.com")
    
    # 2. Check for and bypass a potential Cookie Consent Banner
    try:
        # Looks for the "Accept all" button if it exists
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Accept all") or contains(., "I agree")]'))
        )
        cookie_btn.click()
        print("🍪 >>> Handled cookie consent overlay.")
    except Exception:
        # If no banner popped up, just keep going smoothly
        pass

    print("🔍 >>> Target locked. Finding text input layouts...")
    
    # 3. Securely wait for the real, interactable search box to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    
    print("⌨️ >>> Injecting search sequences dynamically...")
    search_box.click() # Explicitly click it first to force focus
    search_box.send_keys("Your Search Query Here")
    search_box.send_keys(Keys.RETURN)
    
    print("✅ >>> Render complete! Keeping browser alive...")
    time.sleep(400)

except Exception as e:
    print(f"❌ >>> Session aborted due to configuration error: {e}")
finally:
    driver.quit()
    print("🔒 >>> Cloud automation cycle closed successfully.")
    
