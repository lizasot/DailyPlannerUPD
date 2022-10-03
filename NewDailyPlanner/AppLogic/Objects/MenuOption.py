class MenuOption(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        
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