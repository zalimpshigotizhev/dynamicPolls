# dynamicPolls
Динамические опросы с возможностью ветвления исходя из выбранных ответов.
---
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/dynamicPolls.jpg)

# Инструкция по установке
1) Создайте виртуальное окружение и установите requirements.txt.
```cmd
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
``` 
2) Сделайте миграции.
```cmd
python manage.py migrate
```
4) Пропишите команду ниже, чтобы подгрузился готовый опрос для примера.
```cmd
python manage.py seeder
```
4) Запустите сервер и получайте удовольствие от пользование и изучение!
