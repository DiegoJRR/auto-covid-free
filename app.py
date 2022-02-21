from flask import Flask, send_file, request
from flask_restful import Api
import io
import os
from datetime import date

from questionnaire import answer_questionnaire

app = Flask(__name__)
api = Api(app)

@app.route('/')
def test_endpoint():
    return {"hey!": "Nothing to see here"}

@app.route('/cache-driver')
def cache_driver():
    ChromeDriverManager().install()
    return {"cached": "webdriver"}

@app.route('/get-qr')
def get():
    matricula = request.args.get("matricula")
    password = request.args.get("password")
    nombre = request.args.get("nombre")
    telefono = request.args.get("telefono")

    os.environ['TZ'] = 'America/Mexico_City'
    today = date.today()
    # d/m/YY
    date_string = today.strftime("%#d/%#m/%Y")

    qr_image_binary = answer_questionnaire(matricula, password, nombre, telefono, date_string)

    return send_file(
        io.BytesIO(qr_image_binary),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='%s.png' % "QR")


if __name__ == '__main__':
    app.run(debug=True)