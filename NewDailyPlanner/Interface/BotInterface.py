import os

import telebot

from Interface.Base.UserInterface import UserInterface
from AppLogic.CommandHandler import CommandHandler

test_file = 'testsave.json'

file_path = r'D:\MyPr\secretFiles\token.txt'
if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
        token = f.readline()

bot = telebot.TeleBot(token)

class BotInterface(UserInterface):
    #инициализация объекта класса
    def __init__(self):
        self._command_handler = CommandHandler()

    @property
    def command_handler(self):
        return self._content

    #прочее
    def get_name_commands(self):
        return self.command_handler.get_name_commands()

    #стартовая точка программы
    def start(self):
        #Обработка команд с бота
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            bot.reply_to(message, f'sup, {message.from_user.id}')

        @bot.message_handler(func=lambda m: True)
        def echo_all(message):
            bot.reply_to(message, message.text)

        bot.infinity_polling()