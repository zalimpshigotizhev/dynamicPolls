# dynamicPolls
Динамические опросы с возможностью ветвления исходя из выбранных ответов.
---
Проект реализован без использование ORM (Кроме создании таблиц в базе данных), засчет этого можно добиться минимальных запросов от базы данных, что я и постарался сделать. 
После прохождение опроса, показывается статистика по вопросам на которые вы дали ответ. 
   Каждый вопрос имеет нумерацию `numbering` по отсортированному по возрастанию списку.

   
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/pollsDynamic.png)

## Инструменты:
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/python.png) ![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/django.png)
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
   Также сайт является адаптивным. Ниже будут инструкции по пользованию.
   
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/mobile.jpg)

# Как пользоваться приложением
### 1) Создайте образ как это все будет организовано
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/graph.png)

### 2) Придерживаясь этому плану в админ-панеле не спеша состыковывая Choice с Question создавайте вопросы. В админ-панеле есть при создании вопроса графы для варианта ответа тоже, а `next_question` следующий вопрос связывается с вариантом ответа. Если `next_question` не обозначен, то опрос заканчивается и показывается статистика по пройденным вопросам.
![](https://github.com/zalimpshigotizhev/dynamicPolls/blob/main/img_README/result.jpg)
