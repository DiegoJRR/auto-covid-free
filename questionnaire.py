from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
from functools import lru_cache
import os
from datetime import date


from fakeQR import get_fake_qr

@lru_cache(maxsize=10)
def answer_questionnaire(matricula, password, nombre, telefono, date_string):
    print("DID NOT HIT CACHE")
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")
    
    options.binary_location = "opt/google/chrome/chrome"
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    browser.get('https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro')
    browser.implicitly_wait(30)
    
    # Login
    usernameField = browser.find_element_by_name("Ecom_User_ID")
    passwordField = browser.find_element_by_name("Ecom_Password")
    

    usernameField.send_keys(matricula + "@itesm.mx")
    passwordField.send_keys(password)

    browser.find_element_by_id("submitButton").click()
    time.sleep(5)

    # Cuestionario de salud
    try:
        browser.get("https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro#regresoseguroform-Display")
        browser.implicitly_wait(30)
        WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.ID, "__button0-content")))
        browser.find_element_by_id("__button0-content").click()
        time.sleep(2)
        browser.find_element_by_id("__mbox-btn-0-inner").click()
        time.sleep(2)

        pass
    except:
        print("Questionnaire answered already")

    browser.quit()
    
    qr_image_binary = get_fake_qr(matricula, nombre, telefono, date_string)

    return qr_image_binary