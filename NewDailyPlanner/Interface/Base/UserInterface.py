from abc import ABC, abstractmethod, abstractproperty

class UserInterface(ABC):
    @abstractproperty
    def command_handler():
        """обработчик команд"""

    @abstractmethod
    def start():
        """стартовая точка программы"""