from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent


FONT_FILE = ImageFont.truetype(str(BASE_DIR.joinpath('media/cert_gen/font/GreatVibes-Regular.ttf')), 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(str(BASE_DIR.joinpath('media/cert_gen/cert_template/template.png')))
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(str(BASE_DIR.joinpath('media/cert_gen/cert_template/template.png')))
    draw = ImageDraw.Draw(image_source)

    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    fn = name.replace(' ', '_').lower()
    image_source.save(str(BASE_DIR.joinpath('media/cert_gen/cert_temp/')) + '/' + fn +".png")
    print('Saving Certificate of:', name)

if __name__ == "__main__":

    make_certificates('Adeshina Noah')

print(str(BASE_DIR.joinpath('media/cert_gen/cert_temp/')))