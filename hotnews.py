#  Run "crontab -e", then add: "0 1,7,13,19 * * * $USER .~/hotnews/hotrun.sh"

import subprocess
import requests
from datetime import datetime
import pyshorteners
from random import randint
from config import *
from time import sleep
import json

print('''\n
████████████████████████████████████
██ ████▀▄▄▀█▄ ▄█ ▄▄▀█ ▄▄█ ███ █ ▄▄██
██ ▄▄ █ ██ ██ ██ ██ █ ▄▄█▄▀ ▀▄█▄▄▀██
██▄██▄██▄▄███▄██▄██▄█▄▄▄██▄█▄██▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ v0.5 | Mar/2021 ▀▀\n''')
# DEFINE EDITION NUMBER...
hour = datetime.utcnow().hour
if hour >=1 and hour <=6: edition = 1
elif hour >=7 and hour <=12: edition = 2
elif hour >=13 and hour <=18: edition = 3
else: edition = 4
# GENERATE HEADLINES
cc_news = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={ccompare_key}').json()['Data']
headlines = 0
ready_news = []
while headlines < 6:
    update = cc_news[headlines]
    if cc_news[headlines]['source'].title() in str(ready_news):
        cc_news.remove(cc_news[headlines])
    else:
        print(f'Generating metadata for: #{headlines}... ')
        s_adfly = pyshorteners.Shortener(api_key=adfly_key, user_id='24359723', type=3, domain='ad.fly')
        try:
            short_original = pyshorteners.Shortener().isgd.short(update['url'])
        except:
            short_original = pyshorteners.Shortener().dagd.short(update['url'])
        sep = '.jpg' # Remove URL extra parameters
        img_url = update['imageurl']  # Setup an image file
        subprocess.Popen(f'wget {img_url} --tries=10 -nv -q --random-wait -r -O imgs/{headlines}.jpg', shell=True)
        sleep(3)
        publi_time = datetime.utcfromtimestamp(update['published_on'])
        # Setup headline items
        ready_news.append([cc_news[headlines]['id'],  # 0 ID
                           cc_news[headlines]['source'].title(),  # 1 News source
                           cc_news[headlines]['title'],  # 2 Title
                           f'imgs/{headlines}.jpg',  # 3 Jpg format
                           publi_time.strftime("%H:%M UTC | %B, %d"),  # 4 Date
                           s_adfly.adfly.short(update['url']),  # 5 Adfly-url
                           cc_news[headlines]['tags'].replace("|", ","),  # 5 Tags
                           edition,  # 6 Edition number
                           short_original])  # 7 Shorted-url
        headlines += 1
for i in ready_news:
    print(f'\n{i}\n')
# CREATE A SET WITH TAGS (so it doesn't duplicate)
pure_tags = ready_news[0][1]+','+ready_news[1][1]+','+ready_news[2][1]+','+ready_news[3][1]+','+ready_news[4][1]+','+ready_news[5][1]+','+ready_news[0][6]+','+ready_news[1][6]+','+ready_news[2][6]+','+ready_news[3][6]+','+ready_news[4][6]+','+ready_news[5][6]
alltags = set(pure_tags.upper().split(','))
extra_tags = {'KRYPTOKURRENCY', 'KRYPTOWALUTA', 'CRIPTOMONEDA', 'ক্রিপ্টোকারেন্সি', 'КРИПТОВАЛЮТА', 'ΚΡΥΠΤΟΝΌΜΙΣΜΑ', 'КРИПТО ВАЛУТА', 'KRIPTOVALUTA', 'KRÜPTORAHA', 'KRIPTONAUDA', 'CRIPTOMONEDĂ', 'TIỀN ĐIỆN TỬ', 'عملة مشفرة', 'क्रिप्टोकरन्सी', 'КРИПТОВАЛУТА', 'KRIPTO PARA', 'מטבע מוצפן', 'KRIPTOVALUTE', 'CRYPTO-MONNAIE', 'KRYPTOKURRENCY', 'KRYPTOMĚNA', 'KRIPTA MONERO', 'CRIPTOVALUTA', 'CRIPTOMOEDA', 'KRYPTOWÄHRUNG', 'KRIPTOVALUTA', 'κρυπτονόμισμα',
              'БИТКОЙН', 'بيتكوين', 'বিটকয়েন', 'ביטקוין', 'BITKOINAS', 'ബിറ്റ്കോയിൻ', 'बिटकॉइन', 'БИТКОЙН', 'БИТЦОИН', 'பிட்காயின்', 'БІТКОЙН', 'بٹ کوائن'}
youtube_tags = alltags.union(extra_tags)
print(f'Tags with no extras:\n{str(pure_tags)}\n')
with open('data/data.json','w') as json_file:
    json.dump([ready_news, str(youtube_tags), pure_tags[27:].lower()], json_file)
    json_file.close()
# Try running it 3 times...
def really_try(self, times):
    really_done = [False, times]
    while really_done[0] is False:
        if really_done[1] != 0:
            try:
                exec(open(self).read())
                really_done[0] = True
            except:
                really_done[1] -= 1
                print(f'{self} not working, trying again...')
                sleep(30)
        else:
            requests.get('https://api.telegram.org/bot' + telegram_key + '/sendMessage?chat_id=' + '-000000000' + '&parse_mode=Markdown&text=' + f'''
            _HOTNEWS_:
            Error running {self} )''')
            raise EOFError
# GENERATE THUMBNAIL
try:
    exec(open("hotpics.py").read())
except:
    really_try("hotpics.py", 3)
# GENERATE VIDEO
try:
    exec(open("hotvids.py").read())
except:
    really_try("hotvids.py", 3)
# UPLOAD TO YOUTUBE
try:
    exec(open("uploader.py").read())
except:
    really_try("uploader.py", 1)
# COMPLETED OK
print("\nSUCCESSFUL!")
quit()
