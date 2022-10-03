from AppLogic.Objects.MenuOption import MenuOption
from AppLogic.Data.DataKeeper import DataKeeper

class CommandHandler():
    def __init__(self):
        self._menu_options = [MenuOption('mark_completed', 'Отметить задачу выполненной'),
                              MenuOption('add_new_task', 'Добавить новую задачу'),
                              MenuOption('delete_task', 'Удалить задачу'),
                              MenuOption('edit_task', 'Отредактировать задачу'),
                              MenuOption('export_tasks', 'Сохранить задачи в файл'),
                              MenuOption('import_tasks', 'Загрузить задачи из файла')]
        self._data_keeper = DataKeeper()
    @property
    def menu_options(self):
        return self._menu_options

    @property
    def data_keeper(self):
        return self._data_keeper

    #команды обработчика
    def process_command(self, name, params : list = []):
        for x in self.menu_options:
            if x.name == name:
                eval(f'self.{x.name}(params)')
                return 0
        return -1

    def do_by_description_option(self, description : str, params : list = []):
        for x in self.menu_options:
            if description == x.description:
                return self.process_command(x.name, params)
        return -1

    def get_tasks(self, user_id):
        return self.data_keeper.get_uncomplited_tasks_by_id(user_id)

    def get_menu_desriptions(self):
        return [x.description for x in self.menu_options]

    ## команды из меню (должны совпадать с полем name одного из объектов списка menu_options)
    def mark_completed(self, params : list):
        pass

    #params: <user_id>, <new_task_content>
    def add_new_task(self, params : list):
        pass

    def delete_task(self, params : list):
        pass

    def edit_task(self, params : list):
        pass

    def export_tasks(self, params : list):
        pass

    def import_tasks(self, params : list):
        pass