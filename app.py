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

from fakeQR import get_fake_qr

app = Flask(__name__)
api = Api(app)

@app.route('/')
def test_endpoint():
    return {"hey!": "Nothing to see here"}

@app.route('/cache-driver')
def cache_driver():
    ChromeDriverManager(version="98.0.4758.102", cache_valid_range=1).install()

    return {"cached": "webdriver"}

@app.route('/get-qr')
def get():
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
    
    matricula = request.args.get("matricula")
    password = request.args.get("password")
    telefono = request.args.get("telefono")
    nombre = request.args.get("nombre")

    usernameField.send_keys(matricula + "@itesm.mx")
    passwordField.send_keys(password)

    browser.find_element_by_id("submitButton").click()
    time.sleep(5)

    # Cuestionario de salud
    try:
        browser.get("https://flpnwc-aj982psom1.dispatcher.us3.hana.ondemand.com/sites/regresoseguro#regresoseguroform-Display")
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.ID, "__button0-content")))
        browser.find_element_by_id("__button0-content").click()
        time.sleep(1)
        browser.find_element_by_id("__mbox-btn-0-inner").click()
        time.sleep(1)

        pass
    except:
        print("Questionnaire answered already")

    browser.quit()
    
    qr_image_binary = get_fake_qr(matricula, nombre, telefono)

    return send_file(
        io.BytesIO(qr_image_binary),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='%s.png' % "QR")


if __name__ == '__main__':
    app.run(debug=True)