
# Original Hotnews Uploader v0.3 (01/mar/2021)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from datetime import datetime
from time import sleep
import random
import pickle
import json
import os
import subprocess
import requests
from chavs import *

# Loading uploader...
ready_news = json.load(open('data/data.json', 'r'))

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# Starting Firefox headless...
driver.fullscreen_window()
def hold():
    sleep(random.randint(3,9))
# Set tags
ok_tags = str(ready_news[1])[1:-1].replace("'","")
pure_tags = ready_news[2]
# Login and open YoutTube Studio
driver.get('https:\\youtube.com')
# Load cookies, instead of logging in
cookies = pickle.load(open("data/youtube.com.pkl", "rb"))  
for cookie in cookies:
    if 'expiry' in cookie:
        driver.add_cookie(cookie)
        del cookie['expiry']
driver.get('https:\\youtube.com/upload')
hold()
# Upload video file (.mp4)
elem = driver.find_element_by_xpath("//input[@type='file']")
elem.send_keys(os.getcwd() + "/vids/youtube_final.mp4")
sleep(30)
print('Upload... OK')
hold()

random_hello = ['Good to see you','Sup','Aloha','Yo','Greetings','Hello','Salute','Salutations','Hey there',"How's it going?",'Hi','Howdy','Welcome',"What's up",'Hey','Hi-ya','How are you?','How goes it?',"Howdy-do?"]
random_msg = ["The last updates about the cryptocurrency space, every 6 hours!",
              "Be informed and don't miss the bus to the moon!",
              "The best cryptocurrency news for you, 4 times a day!",
              "Get the news from the last 6 hours.",
              "Check the latest updates on the cryptospace.",
              "This channel provides the latest news on crypto every 6 hours.",
              "Don't miss the latest news on crypto.",
              "Obtain the latest news on crypto, in less than a minute!",
              "Enjoy fresh news on cryptocurrency, every 6 hours.",
              "Obtain the latest news in one single minute!",
              'Check the latest reports in the biggest crypto news sites.',
              "Information is power! In this channel you get informed four times a day.",
              "Here you get the best crypto-short-bulletins in the web!",
              "Not financial-advice, financial-intelligence! ;-)",
              "Information is key, don't forget the latest crypto news.",
              "Reporting the cryptocurrency news from the last 6 hours...",
              "Improve your knowledge in crypto with the latest news.",
              "Catch the latest piece of news in the cryptocurrency community.",
              "Earn knowledge, check the last news in the crypto space.",
              "Get updated cryptonews. Get for free!",
              "Hope you enjoy the latest piece of news.",
              "Recent cryptocurrency news, update every six hours.",
              "Enjoy the freshest cryptocurrency news.",
              "Catch crypto updates in one minute, every 6 hours, every day.",
              "Cryptocurrency informations in less than a minute. For free!",
              "Here you gonna find the last news in crypto.",
              "Here is your latest crypto news bulletin.",
              "Check your latest cryptocurrency news bulletin!"]
random_bye = ['Avoid eye contacting the bugs!','Hope you have a nice day! (:','See you soon! LIKE & HODL!',
              'What about sharing some ideas? Leave a note','Do you have some thoughts? Leave a comment',
              "Smile, life's good!",'Spread the message! Share this channel','What about sharing this video?',
              '#LIKE #HODL #UPDATE',"What's on your mind? Share your thoughts","Don't forget to subscribe",
              'Help us spread the news, share it on your preferred social media','Long live Bitcoin!',
              'What do you think? Leave us a hint!','Make your life easier, get advantage, subscribe!',
              'Share your ideas with the community','Hope you can leave a comment','Share your comments',
              'Would be nice to read your comments','Leave a comment and have a nice day!','Like+Share+H0DL',
              'Make sure to share it with your friends!','See you soon. Make sure to share it!']

# Título e descrição
txt_boxes = driver.find_elements_by_xpath('//*[@id="textbox"]')
txt_boxes[0].click()
txt_boxes[0].send_keys(Keys.DELETE*50)
txt_boxes[0].send_keys(Keys.BACKSPACE*50)
txt_boxes[0].send_keys(f'Crypto Flash News | #{ready_news[0][0][7]} Daily Edition ({str(datetime.now())[:10]})')
print('Title OK')
hold()
txt_boxes[0].click()
txt_boxes[1].send_keys(f"""
{random.choice(random_hello)}! {random.choice(random_msg)}
{random.choice(random_bye)}
Check us on Steemit: https://steemit.com/@cryptoflashnews

LINKS:

{ready_news[0][0][2]}
00:04 | {ready_news[0][0][1]} | {ready_news[0][0][5]}

{ready_news[0][1][2]}
00:11 | {ready_news[0][1][1]} | {ready_news[0][1][5]}

{ready_news[0][2][2]}
00:18 | {ready_news[0][2][1]} | {ready_news[0][2][5]}

{ready_news[0][3][2]}
00:25 | {ready_news[0][3][1]} | {ready_news[0][3][5]}

{ready_news[0][4][2]}
00:32 | {ready_news[0][4][1]} | {ready_news[0][4][5]}

{ready_news[0][5][2]}
00:39 | {ready_news[0][5][1]} | {ready_news[0][5][5]}


¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,.¸,ø
D | BTC:
O | 1Fj67dWbeQB2cUG1D4ZGeYvV7KEFBYRVp5
N | DOGE:
A | DNxE1pHk7E89bYEUonwo5hQGugYF6weyVU
T | LTC:
E | LRSq34XgGj8wu2LvzcCDD6muYQfDDJaxJU
`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤º°`°º¤








EXTRA-TAGS:
{ok_tags}

{Keys.TAB}""")
print('Description OK')
# No-kiddo
driver.find_elements_by_xpath('//*[@id="radioLabel"]')[1].click()
print('"Not-for-kids" OK')
# "Mostrar mais"
driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button/div').click()

# Thumbnail upload
hold()
driver.find_element_by_xpath("//input[@id='file-loader']").send_keys(os.getcwd() + "/imgs/thumbnail.jpg")
hold()
print('Thumbnail... OK')
# Add tags
elem = driver.find_elements_by_xpath('//*[@id="text-input"]')
elem[1].send_keys(f'''{ok_tags[0:495]}''')
print('Tags... OK')
# Copy link
ytlink = driver.find_element_by_class_name('style-scope ytcp-video-info').text.rsplit('\n')[2]
hold()
driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div').click()
# Add end-screen
print('Part 2:')
print('  Clicks...')
hold()
driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-video-elements/div[3]/ytcp-button[2]/div').click()
print('     "ADD" button... OK')
hold()
driver.find_element_by_xpath('/html/body/ytve-endscreen-modal/ytve-modal-host/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-endscreen-editor-options-panel/div[1]/ytcp-button[1]/tp-yt-iron-icon').click()
print('     "+" button... OK')
hold()
try:
    driver.find_element_by_xpath('/html/body/ytcp-text-menu[2]/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/div/div/yt-formatted-string').click()
except:
    driver.find_element_by_xpath('/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/div/div/yt-formatted-string').click()
print('     "Video... OK"')
hold()
# add video aos 00:47:05
elem = driver.find_element_by_xpath('/html/body/ytve-endscreen-modal/ytve-modal-host/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-endscreen-editor-options-panel/div[2]/div/ytve-framestamp-input[1]/div/ytve-formatted-input/input')
elem.send_keys(f"{Keys.HOME}47:05")
print('  HOME + "47:05"... OK')
hold()
driver.find_element_by_xpath('/html/body/ytve-endscreen-modal/ytve-modal-host/ytcp-dialog/tp-yt-paper-dialog/div[1]/div/div[2]/div[2]/ytcp-button/div').click()
print('End-screen... OK')
# Set video as public and continue...
hold()
driver.find_element_by_xpath('//*[@id="next-button"]').send_keys(' ')
# Confirm o yayay and continue...
hold()
driver.find_element_by_xpath('//*[@id="next-button"]').send_keys(' ')
hold()
elem = driver.find_elements_by_xpath('//*[@id="offRadio"]')
elem[3].click()
print('Set as public... OK')
hold()
driver.find_element_by_xpath('//*[@id="done-button"]').send_keys(' ')
hold()

print('SUCESS!')

# Avisar pelo telegram
requests.get('https://api.telegram.org/bot' + str(x_7+x_6[::-1]+':'+str(x_2+x_3+x_4+x_5)[::-1]) + '/sendMessage?chat_id=' + '-421478256' + '&parse_mode=Markdown&text=' + f'_HOTNEWS_:\nHotnews {ready_news[0][0][7]} postado!\n{ytlink}\n\nsteemit.com/@cryptoflashnews')

print('Interact with the YouTube video...')
# Open video link, like and interact with links
sleep(5)
driver.get(ytlink)
# Play video
sleep(10)
try:
    driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[30]/div[2]/div[1]/button').click()
    sleep(55)
except:
    pass
# Like video
try:
    driver.find_element_by_class_name('style-scope ytd-toggle-button-renderer').click()
except:
    pass
# Open short URL
driver.get(ready_news[0][0][5])
sleep(60)


# Open and log in Steemit.com
print('Opening Steemit...')
driver.get("https://steemit.com/login.html")
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/form/div[1]/input').send_keys('username')
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/form/div[2]/input').send_keys(steemit_key)
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/form/div[2]/input').send_keys(Keys.ENTER)
sleep(5)
driver.get("https://steemit.com/submit.html")
sleep(3)
# Set title
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/form/div[1]/span/input').send_keys(f'Crypto Flash News | #{ready_news[0][0][7]} Daily Edition ({str(datetime.now())[:10]})')
# Post description
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/form/div[2]/span/div/textarea').send_keys(f"""
{random.choice(random_hello)}!
{random.choice(random_msg)}
6 NEWS FROM THE LAST 6 HOURS:

{ready_news[0][0][2]}
{ready_news[0][0][1]} | {ready_news[0][0][8]}

{ready_news[0][1][2]}
{ready_news[0][1][1]} | {ready_news[0][1][8]}

{ready_news[0][2][2]}
{ready_news[0][2][1]} | {ready_news[0][2][8]}

{ready_news[0][3][2]}
{ready_news[0][3][1]} | {ready_news[0][3][8]}


{ready_news[0][4][2]}
{ready_news[0][4][1]} | {ready_news[0][4][8]}

{ready_news[0][5][2]}
{ready_news[0][5][1]} | {ready_news[0][5][8]})

There's a YouTube channel too:
{ytlink}

{random.choice(random_bye)}
""")
sleep(3)
minitag = [(i) for i in set(pure_tags.lower().split(",")) if len(i)<=8]
othertag = [(i) for i in set(pure_tags.lower().split(",")) if len(i)<=11]
try:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/form/div[4]/span/span/input').send_keys(f'{minitag.pop().lower()} {minitag.pop().lower()} {minitag.pop().lower()}')
except:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/form/div[4]/span/span/input').send_keys(f'{othertag.pop()} {othertag.pop()}')
# Finish
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/form/div[7]/button[1]/span').click()
print('Posted!')
sleep(30)

# Delete geckodriver log and quit!
subprocess.Popen(f'rm geckodriver.log', shell=True)
driver.quit()
