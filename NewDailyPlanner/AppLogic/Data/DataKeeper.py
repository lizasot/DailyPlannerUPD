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
    def get_list_from_file_by_id(self, user_id, file_name):
        if os.path.exists(file_name):
            with open(file_name) as f:
                curr_dict = json.load(f)
        else:
            curr_dict = {}
        if str(user_id) in curr_dict.keys():
            return curr_dict[str(user_id)]
        else:
            return []

    #основные команды
    def get_uncomplited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_uncomplited_tasks)
    
    def get_complited_tasks_by_id(self, user_id):
        return self.get_list_from_file_by_id(user_id, self.save_file_complited_tasks)

    def update_uncomplited_tasks_by_id(self, user_id, tasks : list):
        user_id = str(user_id)
    
    def update_complited_tasks_by_id(self, user_id, tasks : list):
        user_id = str(user_id)