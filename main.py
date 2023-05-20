import random
import requests
from bs4 import BeautifulSoup as b
import telebot


EMAIL_ADDRESS = 'talaydrive@gmail.com'
EMAIL_PASSWORD = 'wrtehlocwkamuyls'

TOKEN='6049827861:AAG9Qs0mYxGS4b3fgK2JI-7uAJl8WNfpqYk'
bot = telebot.TeleBot(TOKEN)
URL = "https://www.anekdot.ru/last/anekdot/"
video_path = r"D:\DOWNLOADS\dark_burb.mp4"
video_path1 = r"D:\DOWNLOADS\brat.MP4"
video_path_maksik = r"D:\DOWNLOADS\maksim_kakaet.mp4"
image_path_kotik_maksik = r"D:\DOWNLOADS\kotik_maksim.jpg"
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,'Привет, но если ты саша то иди ты нахуй черт')
    help(message)
    if message.chat.id == 455657913 :     #455657913
        bot.send_message(message.chat.id, "Нет ты")
        with open(video_path_maksik, 'rb') as video_maksik:
            bot.send_video(message.chat.id, video_maksik)
        with open(image_path_kotik_maksik, 'rb') as photo_kotik_maksik:
            bot.send_photo(message.chat.id, photo_kotik_maksik)


@bot.message_handler(commands=['bobrik'])
def bobrik(message):
    image_path_bobr = r"C:\Users\Артем\PycharmProjects\pythonProject7\bobrik.jpg"
    with open(image_path_bobr, 'rb') as photo_bobr:
        bot.send_photo(message.chat.id,photo_bobr)
        bot.send_message(message.chat.id, 'Скажешь нам что то - получишь в чепчик')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Вот что я умею:\n"
                                     "\n/help - покажу какие есть команды \n"
                                     "/bobrik - фотку бобра покажу \n"
                                     "/start - по стандарту запуск бота \n"
                                     "/restart - еще нету, но будет попозже - перезапуск бота\n"
                                     "/anek - ну анек даст тебе \n"
                                     "/burb - страшилка... \n"
                                     "/bratulets - уйти за бэйб@чк@й \n"
                                     "/porn - для плохих мальчиков \n"
                                     "/xxlporn - рискни... ")

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker = message.sticker
    file_id = sticker.file_id
    image_path = r"C:\Users\Артем\PycharmProjects\pythonProject7\horror.jpg"
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)




@bot.message_handler(commands=['anek'])
def jokes(message):
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]

@bot.message_handler(commands=["porn"])
def porn(message):
    bot.send_message(message.chat.id,"https://m.porno365.pics/random/" )

@bot.message_handler(commands=["xxlporn"])
def xxlporn(message):
    bot.send_message(message.chat.id, 'https://www.porn365.best/tolstushki/')


@bot.message_handler(commands=["burb"])
def burb(message):
    bot.send_message(message.chat.id, "AAAAAAAA")
    with open(video_path, 'rb') as video_burb:
        bot.send_video(message.chat.id, video_burb)

@bot.message_handler(commands=["bratulets"])
def brat(message):
    bot.send_message(message.chat.id, "ну шо ты братулец?! ")
    with open(video_path1, 'rb') as video_bratulets:
        bot.send_video(message.chat.id, video_bratulets)




bot.polling(none_stop=True,interval=0)

