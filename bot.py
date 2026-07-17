from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Route the visual interface directly into our cloud monitor setup
os.environ["DISPLAY"] = ":1"

print("🚀 Initializing cloud-hosted Chrome application...")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    driver.maximize_window()
    
    print("📡 >>> Connecting to network interface...")
    driver.get("https://www.google.com")
    time.sleep(2)
    
    print("🔍 >>> Target locked. Finding text input layouts...")
    search_box = driver.find_element(By.NAME, "q")
    
    print("⌨️ >>> Injecting search sequences dynamically...")
    search_box.send_keys("How to scale a software development agency from a mobile phone")
    time.sleep(1.5)
    
    print("⏩ >>> Submitting execution payload...")
    search_box.send_keys(Keys.RETURN)
    
    print("✅ >>> Render complete! Keeping browser alive on your VNC window...")
    time.sleep(15)

except Exception as e:
    print(f"❌ >>> Session aborted due to configuration error: {e}")

finally:
    driver.quit()
    print("🔒 >>> Cloud automation cycle closed successfully.")
    
