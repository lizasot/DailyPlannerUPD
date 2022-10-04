import json
import os

from config import UNCOMPLITED_TASKS_FILE
from config import COMPLITED_TASKS_FILE

class DataKeeper():
    def __init__(self):
        self._save_file_uncomplited_tasks = UNCOMPLITED_TASKS_FILE
        self._save_file_complited_tasks = COMPLITED_TASKS_FILE

    @property
    def save_file_uncomplited_tasks(self):
        return self._save_file_uncomplited_tasks

    @property
    def save_file_complited_tasks(self):
        return self._save_file_complited_tasks

    #вспомогательные команды
    ##получить список задач по айди
    def get_list_from_file_by_id(self, user_id, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                curr_dict = json.load(f)
        else:
            curr_dict = {}
        if str(user_id) in curr_dict.keys():
            return curr_dict[str(user_id)]
        else:
            return []

    ##обновить список задач по айди
    def update_tasks_file_by_id(self, user_id, file_name, new_tasks : list):
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                curr_dict = json.load(f)
        else:
            curr_dict = {}
        curr_dict[str(user_id)] = new_tasks
        with open(file_name, 'w') as f:
            json.dump(curr_dict, f)
        return 0
    
    #основные команды
    ##получить задачи
    def get_uncomplited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_uncomplited_tasks)
    
    def get_complited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_complited_tasks)
    
    ##обновить задачи
    def update_uncomplited_tasks_by_id(self, user_id, tasks : list):
        return self.update_tasks_file_by_id(user_id, self.save_file_uncomplited_tasks, tasks)
    
    def update_complited_tasks_by_id(self, user_id, tasks : list):
        return self.update_tasks_file_by_id(user_id, self.save_file_complited_tasks, tasks)
        
    ##добавить задачу к существующим
    def add_uncomplited_tasks_by_id(self, user_id, task : str):
        tasks = self.get_uncomplited_tasks_by_id(user_id)
        tasks.append(task)
        return self.update_uncomplited_tasks_by_id(user_id, tasks)

    def add_complited_tasks_by_id(self, user_id, task : str):
        tasks = self.get_complited_tasks_by_id(user_id)
        tasks.append(task)
        return self.update_complited_tasks_by_id(user_id, tasks)

    ##найти задачу в существующих и удалить её
    def del_task_uncomplited_tasks_by_id(self, user_id, ind_task : int):
        tasks = self.get_uncomplited_tasks_by_id(user_id)
        tasks.pop(ind_task)
        return self.update_uncomplited_tasks_by_id(user_id, tasks)

    def del_task_complited_tasks_by_id(self, user_id, ind_task : int):
        tasks = self.get_complited_tasks_by_id(user_id)
        tasks.pop(ind_task)
        return self.update_complited_tasks_by_id(user_id, tasks)

    ##создать файл с задачами
    def create_file_tasks(self, user_id, file_name):
        tasks = self.get_uncomplited_tasks_by_id(user_id)
        return self.update_tasks_file_by_id(user_id, file_name, tasks)

    ##загрузить задачи из файла
    def upload_tasks_from_file(self, user_id, file_name):
        tasks = self.get_list_from_file_by_id(user_id, file_name)
        return self.update_uncomplited_tasks_by_id(user_id, tasks)