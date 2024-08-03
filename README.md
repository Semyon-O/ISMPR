# Проект: Информационная система по управлению заявками и кадровыми ресурсами
## О проекте:
Данный проект представляет собой информационную систему (ИС), цель которой заключается в автоматизации обработки заявок, оптимизации рабочих процессов, а также мониторинг за ходом
выполнение заявок от пользователей системы. Система ориентирована на работу по получениею заявок на телеком.оборудование. 
Данный репозиторий содержит backend часть системы, в которой расписаны API эндпоинты для взаимодействия. 
## Технологии разработки:
- Python (3.10)
- Django (4.37.0)
- DRF

## Установка и запуск:
1. Скачивание
``` git
git clone https://github.com/Semyon-O/ISMPR.git
```
3. Настройка
- Создание окружение
```
python -m venv venv
```
- Активация окружения
``` shell
venv/Scripts/activate (windows)
source venv/bin/activate (Unix)
```
- Скачивание всех библиотек
```
pip install -r requirements.txt
```
- Миграция базы даных (по умолчанию поставлено sqlite)
```
python manage.py makemigrations
python manage.py migrate
```
5. Запуск
```
python manage.py runserver
```

## Превью
![image](https://github.com/user-attachments/assets/864838e9-f2e0-4cb7-b764-2c3c83ba1cb2)
![image](https://github.com/user-attachments/assets/f19218a8-50e9-49a6-9ffe-6cbf91d947f4)
![image](https://github.com/user-attachments/assets/0226cf89-bc92-43d1-a81e-aba42cbaac6e)
![image](https://github.com/user-attachments/assets/51e71e2b-587b-4215-81fd-68a207aec7b4)



