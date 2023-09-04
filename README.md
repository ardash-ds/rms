# Система управления вещами (бэкенд)

Система хранения личных вещей пользователя. 

Сохраняет в базу следующие поля: фото, название, описание, категория, место хранения.

## Установка

1. Склонируйте репозиторий 

```
git clone git@github.com:Ardash12/rms.git
```

2. Установите виртуальное окружение

```
python -m venv venv
```

3. Установите зависимости

```
pip install -r requirements.txt
```

4. Добавьте в корень проекта файл с переменными окружения .env

```
Заполните переменными файл .env_blank и переименуйте его в .env
```

5. Сделайте миграции

```
python manege.py makemigrations categories items storage users
python manege.py migrate
```

6. Заполните бд тестовыми данными

```
python manage.py loaddata ./fixtures/test_data.json
```

7. Запуск сервера

```
python manage.py runserver
```

8. Запуск юнит-тестов 

```
python manage.py test
```

9. Создание суперпользователя для доступа в админку

```
python manage.py createsuperuser
```

Адрес свагера: [http://127.0.0.1:8000/docs/]

Админка: [http://127.0.0.1:8000/admin/]
