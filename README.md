# Ежедневник
Ежедневник позволяет:
- Создавать новые задачи
- Редактировать созданные задачи
- Отмечать их выполненными
- Удалять задачи
- Сохранять и загружать содержание ежедневника в json-файл

Каждая выполненная задача при отметке логируется в текстовый файл с датой и содержанием задачи.

## Установка
Перед запуском проектом выполните команду **pip install -r requirements.txt**, которая подгрузит необходимые для работы приложения модули.

# Консольная версия
![Вид главной страницы ежедневника](/assets/main_screen.jpg)

## Демонстрационные примеры
При открытии ежедневника, если будет найден файл с сохранениями, пользователю будет предложено загрузить ранее сохранённые задачи:

![Предложение загрузить задачи при запуске](/assets/import.jpg)

После того, как задачи будут загружены, они отобразятся на главном экране.


При наличии задач в ежедневнике, пользователь может отмечать их выполненными: 

![Предложение загрузить задачи при запуске](/assets/mark.jpg)

При добавлении новой задачи, пользователь может ввести её название:

![Добавление задачи](/assets/new_task.jpg)

После чего она появится на главном экране:

![Добавленная задача на главном экране](/assets/new_task_result.jpg)

При редактировании и удалении созданных задач, будет аналогичное меню.


Как только одна из задач оказывается отмеченной, она попадает в файл log.txt, дозаписывая в содержимое новые данные. При отсутствии этого файла, создаётся новый.

![Содержимое файла log.txt](/assets/log.jpg)

При сохранении задач, информация о них попадает в файл save.json в следующем виде:

![Содержимое файла save.json](/assets/save.jpg)

# Версия телеграм-бота
Обратите внимания, что для работы бота необходимо создать свой токен для него и поместить его в строке **bot = telebot.TeleBot(token)**

Для старта работы с ботом, используйте команду **/start**.

![Вид меню в боте](/assets/bot_start_menu.jpg)

## Демонстрационные примеры
В случае, если пользователь запросит задачи при их отсутствии, он получит оповещение об этом:

![Оповещение об отсутствии задач](/assets/bot_none_tasks.jpg)

Для добавлении новой задачи необходимо ввести соответствующую команду и её содержание:

![Добавление задачи](/assets/bot_add_task.jpg)

Для удаления же - команду с номером задачи, которую необходимо удалить.

![Удаление задачи](/assets/bot_delete_task.jpg)

Также пользователю доступно изменение уже существующей задачи.

![Редактирование задачи](/assets/bot_edit_task.jpg)

Для пометки задачи как выполненной необходимо ввести соответствующую команду и её номер.

![Выполнение задачи](/assets/bot_mark_task.jpg)
