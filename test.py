from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time






options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Required when running as root user
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:8000/")
    print("Page title:", driver.title)
except Exception as e:
    print("Error accessing the page:", e)
    
