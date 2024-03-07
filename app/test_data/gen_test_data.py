import datetime
from PIL import Image, ImageDraw, ImageFont

def gen_img():
    img = Image.open('./app/test_data/in.png')
    draw = ImageDraw.Draw(img)

    txt = str(datetime.datetime.now())

    myFont = ImageFont.truetype('app/test_data/Lemon Mocktail .ttf', 35)
    draw.text((10, 150), txt, fill =(255, 255, 255), font=myFont)
    img.save(f'app/test_data/output/{txt.replace(" ", "_").replace(":", "-")[:-7]}.png')
    print(txt)
