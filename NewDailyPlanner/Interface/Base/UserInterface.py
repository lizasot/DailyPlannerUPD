from abc import ABC, abstractmethod, abstractproperty

class UserInterface(ABC):
    @abstractproperty
    def command_handler():
        """обработчик команд"""

    @abstractmethod
    def choose_task():
        """запросить у пользователя выбор задачи"""

    @abstractmethod
    def enter_content_task():
        """запросить у пользователя содержание задачи"""

    @abstractmethod
    def start():
        """стартовая точка программы"""