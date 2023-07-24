# Hotpics 0.4

from PIL import Image, ImageOps, ImageDraw, ImageFilter, ImageFont
from datetime import datetime
from time import sleep
from random import randint, choice
import subprocess
import json

ready_news = json.load(open('data/data.json', 'r'))
edition = ready_news[0][0][7]
images = ['imgs/0.jpg','imgs/1.jpg','imgs/2.jpg','imgs/3.jpg','imgs/4.jpg','imgs/5.jpg']
print('\nProcessing images...\n')
# CROP & SCALE images
for i in images:
    try:
        img = Image.open(i).convert('RGB')
        cropped = img.resize((300,300),Image.BOX)
        cropped.save(f'{i}')
    except:
        subprocess.Popen(f'cp imgs/random/rnd{[randint(1,6)]}.jpg {i}', shell=True)
        sleep(1)
        img = Image.open(i).convert('RGB')
        img.save(f'{i}')
colors = ['red','blue','green','yellow','magenta','cyan','purple','orange','white']
bg_img = Image.open(f'imgs/bgs/{randint(1,77)}.jpg').convert('L')
bg_img = ImageOps.colorize(bg_img, black='black', white=choice(colors))
i,j=0,0
# https://stackoverflow.com/questions/10647311/how-do-you-merge-images-into-a-canvas-using-pil-pillow
for num, im in enumerate(images):
    i=(i+212)+2
    j+=1
    sleep(2)
    # Blurring bg images
    blur = Image.open(im)
    blur = ImageEnhance.Color(blur)
    blur = blur.enhance(5).convert("RGB").resize((1280,720), resample=0, box=None).filter(ImageFilter.BoxBlur(333))
    blur.save(f'{im[:-4]}blur.jpg')
    sleep(1)
bg_img.paste(Image.open('imgs/bgs/overlay.jpg'), (360,360))
img_1280 = bg_img.resize((1280,720))
img_final = ImageDraw.Draw(img_1280)
fnt1 = ImageFont.truetype("/usr/share/fonts/gnu-free/FreeMono.otf", 80)
fnt2 = ImageFont.truetype("/usr/share/fonts/gnu-free/FreeMonoBold.otf", 60)
img_final.text((640,450), f'{datetime.now().strftime("%B")},{datetime.now().strftime("%d")}',anchor='mm',
                         align='center', font=fnt1, fill=(255,255,255))
img_final.text((640,560), f'#{edition} Edition',anchor='mm', align='center', font=fnt2, fill=(247,147,26))
img_1280.convert("RGB").save("imgs/thumbnail.jpg", "JPEG", quality=80, optimize=True, progressive=True)
print('Thumbnail OK\n')
