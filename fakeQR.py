import qrcode
from datetime import date
import io
import os 

def get_fake_qr(matricula: str, nombre: str, telefono: str):
    os.environ['TZ'] = 'America/Mexico_City'
    today = date.today()
    
    # d/m/YY
    date_string = today.strftime("%#d/%#m/%Y")

    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            border=5)

    data = f'["{matricula}@itesm.mx","{matricula}","{nombre}","{date_string}","verde","{telefono}","Alumno","Tec de Monterrey","Entrada"]'

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#1d8a18', back_color='white')

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr