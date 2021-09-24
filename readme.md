# Open Lecture script #
## Запуск лекций в один клик ##
__Здесь представлены 3 версии скрипта, написанные для платформы Windows__
## Использование ##
Для работы требуется интерпретатор Python 3 с установленными зависимостями.
## openlecture.py ##
Более упрощенная версия, но не очень удобная. Скрипт содержит встроенное расписание, имя пользователя и не синхронизирован с вашим часовым поясом. Открывает лекции в Zoom и Adobe Connect. Он немного быстрей, чем последующие версии скрипта, но чтобы с ним удобно работать нужно его настроить под себя.
## openlecture2.py ##
Улучшенная версия, здесь решены все проблемы, которые присутсвуют в предыдущей версии. Расписание обновляется по ссылке, которую, при желании, можно заменить на свою, но нужно будет соблюдать JSON формат, как в  представленном `schedule.json`
Имя пользователя вводится при первом запуске и сохраняется в отдельном конфиге для следущих запусков. Расписание `schedule.json` синхронизируется с любым часовым поясом.
## fakesession.py ##
Тоже самое, но открывает лекции в браузере в режиме инкогнито. Бывает полезен когда не хочется чтобы сохранялись куки.

## clearconfig.py ##
Очищает данные и конфиги для `openlecture2.py` и `fakesession.py`

## TO DO: ##
- Скрипт считает и выводит оставшеяся время до лекции, но не считает перерывы между лекциями.
- Возможность открывать по данному предмету курс в moodle
- Auto-mode: добавить запуск и закрытие лекций на текущий день в планировщик задач с автоматическим удалением после выполнения