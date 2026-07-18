import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("🚀 Initializing cloud-hosted Chrome application...")

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--lang=en-US") # Force browser internal language to English

os.environ["DISPLAY"] = ":1"

driver = webdriver.Chrome(options=options)

try:
    driver.set_window_size(1280, 800)
    
    print("📡 >>> Connecting to network interface...")
    # Appending ?hl=en forces Google's search interface into English globally
    driver.get("https://www.google.com?hl=en")
    
    # Handle cookie banners by element ID rather than text matching
    try:
        cookie_btn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="L2AGLb"] | //button[contains(., "Accept all")]'))
        )
        cookie_btn.click()
        print("🍪 >>> Handled regional cookie consent overlay.")
    except Exception:
        pass

    print("🔍 >>> Target locked. Finding text input layouts...")
    
    # Wait until the search box exists in the document
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    print("⌨️ >>> Injecting search sequences dynamically...")
    # Typing directly without using .click() prevents ElementClickIntercepted errors
    search_box.clear()
    search_box.send_keys("Python automation workflows")
    search_box.send_keys(Keys.RETURN)
    
    print("✅ >>> Render complete! Keeping browser alive...")
    time.sleep(400)

except Exception as e:
    print(f"❌ >>> Session aborted due to configuration error: {e}")
finally:
    driver.quit()
    print("🔒 >>> Cloud automation cycle closed successfully.")
    
