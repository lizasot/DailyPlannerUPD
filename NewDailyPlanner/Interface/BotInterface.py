from ast import If
import os

import telebot

from Interface.Base.UserInterface import UserInterface
from AppLogic.CommandHandler import CommandHandler

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
        return self._command_handler

    #прочее
    def get_name_commands(self):
        return self.command_handler.get_name_commands()

    def choose_task(self):
        """запросить у пользователя выбор задачи"""
        
    def enter_content_task(self):
        """запросить у пользователя содержание задачи"""

    #команды возвращающие строки
    def display_tasks(self, user_id):
        tasks = self.command_handler.get_tasks(user_id)
        task_str = ''
        if len(tasks) > 0:
            for x in range(0, len(tasks)):
                task_str += f'{x + 1}. {tasks[x]}\n'
        else:
            task_str += 'На данный момент у вас нет задач.'
        return task_str

    #стартовая точка программы
    def start(self):
        #Обработка команд с бота
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            menu = self.command_handler.get_menu_desriptions()
            menu_str = ''
            for x in range(0, len(menu)):
                name_menu = self.command_handler.get_name_by_description_option(menu[x])
                menu_str += f'{menu[x]}: /{name_menu}'
                request_for_params = self.command_handler.check_which_parameters_for_command(name_menu)
                for x in request_for_params:
                    if x == 'choose_task':
                        menu_str += ' <номер_задачи>'
                    elif x == 'enter_content_task':
                        menu_str += ' <содержание>'
                menu_str += '\n'
            menu_str += 'Посмотреть текущие задачи: /view_tasks'
            bot.reply_to(message, menu_str)

        @bot.message_handler(commands=['view_tasks'])
        def view_tasks(message):
            task_str = self.display_tasks(message.from_user.id)
            bot.reply_to(message, task_str)

        @bot.message_handler(func=lambda m: True)
        def echo_all(message):
            params = message.text.split()
            params[0] = params[0][1:]
            option = params.pop(0)
            request_for_params = self.command_handler.check_which_parameters_for_command(option)
            numb = -1
            text = ''
            success = True
            for x in request_for_params:
                if x == 'choose_task':
                    if len(params) > 0 and params[0].isdigit():
                        numb = params.pop(0)
                    else:
                        success = False
                        break
                elif x == 'enter_content_task':
                    if len(params) > 0:
                        text = ' '.join(params)
                    else:
                        success = False
            params.clear()
            if numb != -1:
                params.append(numb)
            if text != '':
                params.append(text)
            if success:
                self.command_handler.process_command(option, params, message.from_user.id)
                bot.reply_to(message, 'Успешно.')
            else:
                bot.reply_to(message, 'Ошибка. Не указаны какие-то параметры. Воспользуйтесь командой /help для справки.')

        bot.infinity_polling()