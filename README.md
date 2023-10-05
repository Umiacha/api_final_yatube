<h1 align="center"><b>Описание</b></h1>
REST-сервис, написанный с помощью Django REST framework. Он позволяет создавать, получать или изменять записи, а также оставлять комментарии "под ними" и оформлять подписки на пользователей (правда последнее пока что бесполезно).
<h1 align="center"><b>Установка</b></h1>
Клонируйте репозиторий:        

```
git clone git@github.com:Umiacha/api_final_yatube.git
```

Перейдите в директорию проекта:        

```
cd api_final_yatube
```

Установить виртуальное окружение:        

```
python3 -m venv venv
```

И активировать его (пример для bash):        

```
. venv/bin/activate
```

Установить зависимости из файла requirements.txt:        

```
pip install -r requirements.txt
```

Выполнить миграции:        

```
python manage.py migrate
```

Запустить проект:        

```
python manage.py runserver
```

<h1 align="center"><b>Примеры запросов</b></h1>
Для получения списка эндпоинтов с полным описанием поведения сервиса можно открыть в браузере страницу redoc/ по url-адресу запущенного сервиса.
Для меня это:        

```
https://127.0.0.1:8000/redoc/
```
А благодаря <a href="https://www.django-rest-framework.org/topics/browsable-api/">Browsable API</a> можно отправлять запросы и читать ответы прямо в браузере. Для этого достаточно открыть желаемый URL-адрес в отдельной вкладке.
