from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from django.conf import settings
import pyqrcode
import png
from pyqrcode import QRCode

BASE_DIR = Path(__file__).resolve().parent.parent


FONT_FILE = ImageFont.truetype(str(BASE_DIR.joinpath('media/cert_gen/font/GreatVibes-Regular.ttf')), 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(str(BASE_DIR.joinpath('media/cert_gen/cert_template/template.png')))
WIDTH, HEIGHT = template.size

def make_certificates(name, url):
    '''Function to save certificates as a .png file'''
    vfn = make_qrcode(url)
    v_img = Image.open(vfn)

    image_source = Image.open(str(BASE_DIR.joinpath('media/cert_gen/cert_template/template.png')))
    draw = ImageDraw.Draw(image_source)
    image_source.paste(v_img, (1500, 950))

    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    fn = name.replace(' ', '_').lower()
    image_source.save(str(BASE_DIR.joinpath('media/cert_gen/cert_temp/')) + '/' + fn +".png")
    print('Saving Certificate of:', name)

def make_qrcode(url):
    url = pyqrcode.create(url)
    
    # Create and save the png file naming "myqr.png"
    url.png(str(BASE_DIR.joinpath('media/qrcode/'))+ '/' + 'veri.png', scale = 12)
    vfn = str(BASE_DIR.joinpath('media/qrcode/'))+ '/' + 'veri.png'
    return vfn

if __name__ == "__main__":

    make_certificates('Adeshina K Noah', 'google.com')

    # make_qrcode('google.com')