import telebot, random
from telebot import types
import datetime as dt

bot = telebot.TeleBot("2126010966:AAF6BIrshew-UuJwdxNHEkWN5rNuGNFXxgI")

audio_url = 'https://cs1-52v4.vkuseraudio.net/p5/579285436a3ee3.mp3?extra=..'
audio_url_1 = 'https://cs1-46v4.vkuseraudio.net/p8/7be4a9af843d3e.mp3?extra=..'
audio_url_2 = 'https://cs1-67v4.vkuseraudio.net/p6/e850bde7cb40ba.mp3?extra=..'


list = [audio_url, audio_url_1, audio_url_2]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("хочу", "/help",'/music_random','/time')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! I am simple bot.\n'
                                    'You can control me by sending these commands:\n\n'
                                    '/music_random - случайная музыка\n'
                                    '/time - текущее время и дата\n')


@bot.message_handler(commands=['music_random'])
def audio(message):
    bot.send_audio(chat_id=message.chat.id, audio=random.choice(list))


@bot.message_handler(commands=['time'])
def message_time(message):
    source_date = dt.datetime.now()
    bot.send_message(message.chat.id, source_date)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'хочу':
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://mtuci.ru/')

bot.polling(none_stop=True, interval=0)