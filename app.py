from flask import Flask, send_file, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager

from flask_restful import Api
import io

app = Flask(__name__)
api = Api(app)

@app.route('/get-qr')
def get():
    options = Options()
    options.headless = True
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu-sandbox')
    options.add_argument("--single-process")
    options.add_argument(
    '"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"')
    options.add_argument("--log-level=0")
    options.add_argument("--single-process")
    options.add_argument("--ignore-certificate-errors")

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro')
    browser.implicitly_wait(30)

    # Login
    usernameField = browser.find_element_by_name("Ecom_User_ID")
    passwordField = browser.find_element_by_name("Ecom_Password")
    
    usernameField.send_keys(request.args.get("email"))
    passwordField.send_keys(request.args.get("password"))

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
    qr_image_binary = browser.get_screenshot_as_png()

    return send_file(
        io.BytesIO(qr_image_binary),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='%s.png' % "QR")


if __name__ == '__main__':
    app.run(debug=True)