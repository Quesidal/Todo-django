# Todo-django
Python 3.6 + Django

Установка:
1. Установите Python 3.6 https://www.python.org/
2. Скачайте проект и поместите в удобную вам директорию
3. Установите необходимые модули 
```pip3 install -r requirements.txt```


Запуск проекта:
1. Перейдите в главную директорию проекта
2. Создайте базу данных применив миграции
```python manage.py migrate```
3. Запустите сервер командой
```py manage.py runserver```
4. После запуска, доступ к сайту можно будет получить по адресу http://127.0.0.1:8000/


Дополнительные команды:
1. ```python manage.py setup_test_date``` - генерирует тестовый датасет(1 пользователь 4 проекта 40 задач)
2. ```python manage.py gen_users``` - создает 2 новых пользователя
3. ```python manage.py gen_projects``` - создает 4 новых проекта
4. ```python manage.py gen_tasks``` - создает 10 новых задач

Пример использования:
- Запустите проект
- Создайте тестовый датасет командой `python manage.py setup_test_date`
```
python manage.py setup_test_date

# Project1  Johnson-Briggs
# ...
# Task16  Sign if dream imagine after knowledge themselves. ...
# ...
# User1  username: Shane1  password: Shane1````
```

- Перейдите на главную страницу проекта, и войдите с тестовыми даными

Задеплоеный проект на Heroku https://test-task-todo.herokuapp.com

~~~~
- Username: Ashley0
- Password: Ashley0