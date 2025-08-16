from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = Options()

# Headless mode and essential arguments
options.add_argument("--headless=new")  # for Chrome 109+
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=C:/tmp/selenium")  # ensure this folder exists

# Optional: prevent automation detection (can help with some sites)
options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Sample URL — change to your target page
url = "https://www.hackerrank.com/"  # Replace with the real target page if different
driver.get(url)

# Wait for page to load (adjust as needed)
time.sleep(3)

# Example: Extract titl
