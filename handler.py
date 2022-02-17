from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time

load_dotenv(".env")

options = Options()
# options.headless = True

chromedriver = 'chromedriver.exe'
browser = webdriver.Chrome(chromedriver, options=options)
browser.get('https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro')
browser.implicitly_wait(30)

# Login
username = browser.find_element_by_name("Ecom_User_ID")
password = browser.find_element_by_name("Ecom_Password")

username.send_keys(os.getenv("EMAIL"))
password.send_keys(os.getenv("PASSWORD"))
browser.find_element_by_id("submitButton").click()
time.sleep(5)


# Cuestionario de salud
# browser.get("https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro#regresoseguroform-Display")
# WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.ID, "__button0-content")))
# browser.find_element_by_id("__button0-content").click()
# time.sleep(1)
# browser.find_element_by_id("__mbox-btn-0-inner").click()
# time.sleep(2)

# QR 
browser.get("https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro#qr-Display")
browser.set_window_size(400, 800)
WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.ID, "__data48")))

# Screenshot
browser.save_screenshot("screenshot.png")