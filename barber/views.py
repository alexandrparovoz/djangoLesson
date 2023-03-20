from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def index(request):
    posts = Barber.objects.all()
    return render(request, 'barber/index.html', {'posts': posts})

def about(request):
    return render(request, 'barber/about.html')


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def category(request, catid):
    return HttpResponse(f'<h2>Это страница категорий</h2>{catid}</p>')

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)                        #raise Http404
    # if request.GET:
    #     print(request.GET)
    return HttpResponse(f'<h2>Это страница архива</h2>{year}</p>')


def  pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2>Этa страница не найдена</h2>')
