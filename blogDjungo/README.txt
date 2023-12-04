---------------------------------- СОЗДАЕМ ФУНКЦИОНАЛ (БЛОГ)

Создаем свой блог
python manage.py startapp blog

После того, как приложение создано, нам нужно сообщить Django, что теперь он должен его использовать. Мы сделаем это с помощью файла mysite/settings.py. Нам нужно найти INSTALLED_APPS и добавить к списку 'blog', прямо перед ]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]


В файле blog/models.py мы определяем все Модели

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model): — эта строка определяет нашу модель (объект).

class — ключевое слово для определения объектов
Post — имя нашей модели, можем менять
models.Model - объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных
задаем свойства: title, text, created_date, published_date, author
models.CharField — так мы определяем текстовое поле с ограничением на количество символов
models.TextField — так определяется поле для неограниченно длинного текста
models.DateTimeField — дата и время
models.ForeignKey — ссылка на другую модель
https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types

def publish(self): - метод публикации для записи, publish — это название этого метода, можно изменить
метод __str__ после вызова метода __str__() мы получим текст (строку) с заголовком записи


добавление нашей модели в базу данных
дать Django знать, что сделали изменения в нашей модели (мы её только что создали)
python manage.py makemigrations blog

проверка
python manage.py migrate blog

можно админить
http://127.0.0.1:8000/admin/

создаем в консоле админа
python manage.py createsuperuser

Чтобы работать с записями, для которых мы только что создали модель, используем панель управления администратора Django
в blog/admin.py:
from django.contrib import admin
from .models import Post
admin.site.register(Post)

(admin, 123)

Файл mysite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

Создай новый пустой файл blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]


Создаем вью: blog/views.py

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


Шаблоны сохраняются в директории blog/templates/blog
создай файл post_list.html

---------------------------------- РАБОТАЕМ С КОНСОЛЬЮ ДЖАНГО

запуск консоли Django
python manage.py shell

импорт моделей
from blog.models import Post

просмотр моделей
Post.objects.all()
Post.objects.filter(author=me) - фильтрация записей
Post.objects.filter(title__contains='title') - поиск по заголовку

просмотр всех опубликованных записей
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())

импорт пользователей
from django.contrib.auth.models import User
просмотр пользователей
User.objects.all()

создаем пользователя нам
me = User.objects.get(username='admin')
Post.objects.create(author=me, title='Тест консоль', text='Создаем запись из консоли')

опубликуем созданную запись
post = Post.objects.get(title="Тест консоль")
post.publish()

сортировка
Post.objects.order_by('created_date')
Post.objects.order_by('-created_date') - в обратном порядке

---------------------------------- ШАБЛОНЫ

переменные в шаблоне в {{ name }}
{{ posts }}

выводим все
  {% for post in posts %}
    <div>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaksbr }}</p>
        <p>опубликовано: {{ post.published_date }}</p>
    </div>
    {% endfor %}


добавим CSS
в корне в "blog": static/css/blog.css

имзеняем шаблон
{% load static %}
<html>
    <head>
        <title>Django Blog</title>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>

        {% for post in posts %}
            <div>
                <h2><a href="">{{ post.title }}</a></h2>
                <p>{{ post.text|linebreaksbr }}</p>
		<p>опубликовано: {{ post.published_date }}</p>
            </div>
        {% endfor %}
    </body>
</html>

---
делаем общий шаблон для нескольких страниц: base.html

{% load static %}
<html>
    <head>
        <title>Django Blog</title>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
<body>
    <div class="page-header">
        <h1><a href="/">Django Blog</a></h1>
    </div>
    <div>
            {% block content %}
            {% endblock %}
    </div>
</body>
</html>

используем его где надо: post_list.html
в ссылку сделал адрес через primary key записи

{% extends 'blog/base.html' %}

{% block content %}
	{% for post in posts %}
            <div>
                <h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
                <p>{{ post.text|linebreaksbr }}</p>
		<p>опубликовано: {{ post.published_date }}</p>
            </div>
        {% endfor %}
{% endblock %}

в urls.py надо добавить адрес для чтения записей

from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #добавили
]

в views.py надо прописать шаблоны для чтения записи

from django.shortcuts import render, get_object_or_404 #добавили get_object_or_404
from django.utils import timezone
from .models import Post 

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#добавили описание
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

создаем шаблон в templates для просмотра записей post_detail.html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}

---------------------- ИНСТРУМЕНТ ДОБАВЛЕНИЯ ЗАПИСЕЙ В БЛОГ

В urls.py добавляем
path('post/new/', views.post_new, name='post_new'),

в views.py добавляем
from .forms import PostForm
from django.shortcuts import redirect

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


в templates создаем шаблон для добавления записи post_edit.html
{% extends 'blog/base.html' %}

{% block content %}
    <h2>Добавить новую запись</h2>
    <form method="POST">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Сохранить</button>
    </form>
{% endblock %}

-------------------------------------------ДОБАВЛЯЕМ РЕДАКТИРОВАНИЕ ЗАПИСЕЙ

ссылка на редактирование в post_detail.html
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">редактировать</span></a>

добавляем путь в urls.py
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

добавляем в views.py
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

------------------------------ ОБЕЗАПАСИМ ВСЕ, ДОБАВЛЕНИЕ ТОЛЬКО ТЕМ, КТО АВТОРИЗОВАЛСЯ

в post_list.html, где ссылка, выводим ее через условие
{% if user.is_authenticated %}
    <a href="{% url 'post_new' %}">добавить</span></a>
{% endif %}

аналогично и с редактированием в post_detail.html