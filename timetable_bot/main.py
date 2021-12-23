import telebot
import psycopg2
from telebot import types
import datetime

token = '5020047153:AAGuPuxqOi0NRRjzFTZBdq2OaiBg1Navvt0'
bot = telebot.TeleBot(token)

conn = psycopg2.connect(database='dz_db',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432')


def execute_read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

week = datetime.date.today().isocalendar()[1]


def vn():
    if week % 2 == 0:
        return 'n'
    if week % 2 == 1:
        return 'v'


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница")
    keyboard.add('Расписание на текущую неделю')
    keyboard.add('Расписание на следующую неделю')
    bot.send_message(message.chat.id, "На какой день недели интересует расписание?", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Команды:\n"
                                        "/now_week - Какая сейчас неделя?")

@bot.message_handler(commands=['now_week'])
def now_week(message):
    if vn() == 'v':
        bot.send_message(message.chat.id, "Сейчас верхняя неделя")
    elif vn() == 'n':
        bot.send_message(message.chat.id, "Сейчас нижняя неделя")

@bot.message_handler(content_types=['text'])
def xxx(message):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    final = []
    if message.text == "Понедельник" or message.text == "Вторник" or message.text == "Среда" or message.text == "Четверг" or message.text == "Пятница":
        day = message.text

        if vn() == 'n':
            result = []
            select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE vn = 'n' OR vn = 'vn'"
            timetable = execute_read_query(conn, select_timetable)
            for i in timetable:
                if i[0] == day:
                    for j in i:
                        if j == day:
                            continue
                        else:
                            result.append(str(j)+' ')
                    result.append('\n')
            bot.send_message(message.chat.id, '_____' + day + '_____' + '\n' + '\n' + ''.join(result))

        if vn() == 'v':
            result = []
            select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE vn = 'v' OR vn = 'vn'"
            timetable = execute_read_query(conn, select_timetable)
            for i in timetable:
                if i[0] == day:
                    for j in i:
                        if j == day:
                            continue
                        else:
                            result.append(str(j)+' ')
                    result.append('\n')
            bot.send_message(message.chat.id, '_____' + day + '_____' + '\n' + '\n' + ''.join(result))

        elif message.text == 'Расписание на текущую неделю':

            if vn() == 'n':
                select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE vn ='n' OR vn = 'vn'"
                timetable = execute_read_query(conn, select_timetable)
                for day in days:
                    result = []
                    for i in timetable:
                        if i[0] == day:
                            for j in i:
                                 if j == day:
                                     continue
                                 else:
                                    result.append(str(j)+' ')
                        result.append('\n')
                    final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
                bot.send_message(message.chat.id, ''.join(final))

            if vn() == 'v':
                select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE vn = 'v' OR vn = 'vn'"
                timetable = execute_read_query(conn, select_timetable)
                for day in days:
                    result = []
                    for i in timetable:
                        if i[0] == day:
                            for j in i:
                                if j == day:
                                    continue
                                else:
                                    result.append(str(j) + ' ')
                        result.append('\n')
                    final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
                bot.send_message(message.chat.id, ''.join(final))

        elif message.text == 'Расписание на следующую неделю':
            if vn() == 'v':
                select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE (vn = 'n' OR vn = 'vn')"
                timetable = execute_read_query(conn, select_timetable)
                for day in days:
                    result = []
                    for i in timetable:
                        if i[0] == day:
                            for j in i:
                                if j == day:
                                    continue
                                else:
                                    result.append(str(j) + ' ')
                            result.append('\n')
                    final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
                bot.send_message(message.chat.id, ''.join(final))

            if vn() == "n":
                select_timetable = "SELECT day, subject, room_numb, start_time FROM timetable WHERE (vn = 'v' OR vn = 'vn')"
                timetable = execute_read_query(conn, select_timetable)
                for day in days:
                    result = []
                    for i in timetable:
                        if i[0] == day:
                            for j in i:
                                if j == day:
                                    continue
                                else:
                                    result.append(str(j) + ' ')
                            result.append('\n')
                    final.append('_____' + day + '_____' + '\n' + '\n' + ''.join(result) + '\n')
                bot.send_message(message.chat.id, ''.join(final))

    else:
        bot.send_message(message.chat.id, 'Я Вас не понял. Повторите запрос.')

bot.polling()