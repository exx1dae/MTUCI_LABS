import telebot
from telebot import types
import psycopg2

token = '5020047153:AAGuPuxqOi0NRRjzFTZBdq2OaiBg1Navvt0'
bot = telebot.TeleBot(token)

conn = psycopg2.connect(database='bot_db',
                        user = 'postgres',
                        host = 'localhost',
                        port = '5432')

cursor = conn.cursor()

