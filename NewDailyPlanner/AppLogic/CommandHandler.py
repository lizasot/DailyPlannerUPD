from config import FILE_FOR_EXPORT
from config import FILE_FOR_IMPORT
from AppLogic.Objects.MenuOption import MenuOption
from AppLogic.Data.DataKeeper import DataKeeper

class CommandHandler():
    def __init__(self):
        self._menu_options = [MenuOption('mark_completed', 'Отметить задачу выполненной', True, False),
                              MenuOption('add_new_task', 'Добавить новую задачу', False, True),
                              MenuOption('delete_task', 'Удалить задачу', True, False),
                              MenuOption('edit_task', 'Отредактировать задачу', True, True),
                              MenuOption('export_tasks', f'Сохранить задачи в файл {FILE_FOR_EXPORT}'),
                              MenuOption('import_tasks', f'Загрузить задачи из файла {FILE_FOR_IMPORT}')]
        self._data_keeper = DataKeeper()
    @property
    def menu_options(self):
        return self._menu_options

    @property
    def data_keeper(self):
        return self._data_keeper

    #команды обработчика
    def check_which_parameters_for_command(self, name_command):
        params : list = []
        for x in self.menu_options:
            if x.name == name_command:
                if x.index_task:
                    params.append('choose_task')
                if x.content_str:
                    params.append('enter_content_task')
                break
        return params

    def process_command(self, name_command, params : list = [], user_id = -1):
        for x in self.menu_options:
            if x.name == name_command:
                return eval(f'self.{x.name}(params, user_id)')
        return -1

    def get_name_by_description_option(self, description : str):
        for x in self.menu_options:
            if description == x.description:
                return x.name
        return -1

    def get_tasks(self, user_id = -1):
        return self.data_keeper.get_uncomplited_tasks_by_id(user_id)

    def get_menu_desriptions(self):
        return [x.description for x in self.menu_options]
    
    ## команды из меню (должны совпадать с полем name одного из объектов списка menu_options)
    def mark_completed(self, params : list, user_id):
        if len(params) > 0:
            tasks = self.get_tasks(user_id)
            task = tasks.pop(int(params[0]))
            self.data_keeper.log_complited_task(user_id, task)
            self.data_keeper.add_complited_tasks_by_id(user_id, task)
            return self.data_keeper.update_uncomplited_tasks_by_id(user_id, tasks)
        return -1
    
    def add_new_task(self, params : list, user_id):
        if len(params) > 0:
            return self.data_keeper.add_uncomplited_tasks_by_id(user_id, params[0])
        return -1

    def delete_task(self, params : list, user_id):
        if len(params) > 0:
            return self.data_keeper.del_task_uncomplited_tasks_by_id(user_id, int(params[0]))
        return -1

    def edit_task(self, params : list, user_id):
        if len(params) > 0:
            tasks = self.get_tasks(user_id)
            tasks[int(params[0])] = str(params[1])
            return self.data_keeper.update_uncomplited_tasks_by_id(user_id, tasks)
        return -1

    def export_tasks(self, params : list, user_id):
        return self.data_keeper.create_file_tasks(user_id, FILE_FOR_EXPORT)

    def import_tasks(self, params : list, user_id):
        return self.data_keeper.upload_tasks_from_file(user_id, FILE_FOR_IMPORT)