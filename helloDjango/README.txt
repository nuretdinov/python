1. Cоздаем директорию для проекта helloDjango
2. Запускаем командную строку: win+r -> cmd
3. Переходим в директорию: cd путь_к_helloDjango
4. Cоздадим виртуальное окружение: python -m venv myvenv
5. запуск виртуального окружения: myvenv\Scripts\activate
6. Установка Django: pip install Django
7. Создайте новый проект Django: django-admin startproject hiProject
8. Создайте новое приложение Django: python manage.py startapp myapp

9. Настраиваем контроллер проекта:

#hiProject urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

10. Настраиваем контроллер приложения:

#myapp urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('bye/', views.bye, name='bye'),
]

11. Настраиваем вью (представление):

from django.shortcuts import render
from django.http import HttpResponse 

def hello(request):
	return HttpResponse("Hello, World!")

def bye(request):
	return HttpResponse("Bye!")

12. Запускаем сервер: python manage.py runserver
13. Смотрим результат: http://127.0.0.1:8000/ и http://127.0.0.1:8000/buy