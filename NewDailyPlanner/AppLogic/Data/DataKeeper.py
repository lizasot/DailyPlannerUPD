import json
import os

class DataKeeper():
    def __init__(self):
        self._save_file_uncomplited_tasks = 'uncomplited_tasks.txt'
        self._save_file_complited_tasks = 'complited_tasks.txt'

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
    
    #основные команды
    ##получить задачи
    def get_uncomplited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_uncomplited_tasks)
    
    def get_complited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_complited_tasks)
    
    ##обновить задачи
    def update_uncomplited_tasks_by_id(self, user_id, tasks : list):
        self.update_tasks_file_by_id(user_id, self.save_file_uncomplited_tasks, tasks)
    
    def update_complited_tasks_by_id(self, user_id, tasks : list):
        self.update_tasks_file_by_id(user_id, self.save_file_complited_tasks, tasks)
        
    ##добавить задачу к существующим
    def add_uncomplited_tasks_by_id(self, user_id, task : str):
        tasks = self.get_uncomplited_tasks_by_id(user_id)
        tasks.append(task)
        tasks = self.update_uncomplited_tasks_by_id(user_id, tasks)

    def add_complited_tasks_by_id(self, user_id, task : str):
        tasks = self.get_complited_tasks_by_id(user_id)
        tasks.append(task)
        tasks = self.update_complited_tasks_by_id(user_id, tasks)

    ##найти задачу в существующих и удалить её
    def del_task_uncomplited_tasks_by_id(self, user_id, ind_task : int):
        tasks = self.get_uncomplited_tasks_by_id(user_id)
        tasks.pop(ind_task)
        tasks = self.update_uncomplited_tasks_by_id(user_id, tasks)

    def del_task_complited_tasks_by_id(self, user_id, ind_task : int):
        tasks = self.get_complited_tasks_by_id(user_id)
        tasks.pop(ind_task)
        tasks = self.update_complited_tasks_by_id(user_id, tasks)