class MenuOption(object):
    def __init__(self, name, description, index_task = False, content_str = False):
        self._name = name
        self._description = description
        self._index_task = index_task
        self._content_str = content_str
        
    #full_name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is str:
            self._name = name
        
    #command
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description is str:
            self._description = description

    #need params
    ##index_task
    @property
    def index_task(self):
        return self._index_task

    @index_task.setter
    def index_task(self, index_task):
        if index_task is bool:
            self._index_task = index_task

    ##content_str
    @property
    def content_str(self):
        return self._content_str

    @content_str.setter
    def content_str(self, content_str):
        if content_str is bool:
            self._content_str = content_str