from time import sleep

import keyboard

from Interface.Base.UserInterface import UserInterface
from AppLogic.CommandHandler import CommandHandler

class ConsoleInterface(UserInterface):
    #инициализация объекта класса
    def __init__(self):
        self._command_handler = CommandHandler()
        self._user_id = '1'

    @property
    def command_handler(self):
        return self._command_handler

    @property
    def user_id(self):
        return self._user_id

    #вспомогательные команды
    def clear(self):
        print('\n' * 100)

    def get_choice(self):
        sleep(0.3)
        key = keyboard.read_key()
        while key != 'up' and key != 'down' and key != 'enter':
            key = keyboard.read_key()
        if key == 'up':
            return -1
        elif key == 'down':
            return 1
        elif key == 'enter':
            input()
            return 0

    #команды для вывода данных
    def print_list(self, options : list, select_ind : int):
        if len(options) > 0:
            for x in range(0, len(options)):
                if x == select_ind:
                    print('[*]', end='')
                else:
                    print('[ ]', end='')
                print(options[x])
                
    def choice_handler(self, choice : int, choice_ind : int, l : list):
        if choice == -1 and choice_ind != 0:
            choice_ind -= 1
        elif choice == 1 and choice_ind != len(l) - 1:
            choice_ind += 1
        return choice_ind

    def get_option(self, options : list, repeat):
        choice = 1
        choice_ind = 0
        while choice != 0:
            self.clear()
            repeat()
            self.print_list(options, choice_ind)
            choice = self.get_choice()
            if choice != 0:
                choice_ind = self.choice_handler(choice, choice_ind, options)
        return options[choice_ind]

    def display_tasks(self, select_ind : int = -1):
        tasks = self.command_handler.get_tasks(self.user_id)
        if len(tasks) > 0:
            self.printList(tasks)
            print('=================')

    def display_menu(self, select_ind : int):
        options = self.command_handler.get_tasks(self.user_id)
        if options > 0:
            for x in range(0, len(options)):
                if x == select_ind:
                    print('[*]', end='')
                else:
                    print('[ ]', end='')
                print(options[x])

    #стартовая точка программы
    def start(self):
        end = False
        while not end:
            text_for_repeat = lambda: self.display_tasks()
            option = self.get_option(self.command_handler.get_menu_desriptions(), text_for_repeat)