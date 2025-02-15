from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse


menu = [
    {'title': 'About site','url_name': 'about_site'},
    {'title': 'Add a page','url_name': 'add_page'},
    {'title':'feedback','url_name':'feedback'},
    {'title':'Login','url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):# HttpRequest
    main = {'title': 'Main application women.',
            'menu': menu,
            'data': data_db,
            }
    return render(request,'women/index.html',context = main)


def about(request):
    data = {'title':'About application women.',
             'menu':menu,
            'data':data_db,
            }
    return render(request,'women/about.html',data)

def show_post(request,post_id):
    return HttpResponse(f"Отображение статьей с id = {post_id}")


def add_page(request):
    return HttpResponse('Добавление статьи.')


def login(request):
    return HttpResponse('Авторизация.')


def feedback(requests):
    return  HttpResponse('Обратная связь.')

