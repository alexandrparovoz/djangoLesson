from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def index(request):
    posts = Barber.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }

    return render(request, 'barber/index.html', context=context)


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

def show_category(request, cat_id):
    posts = Barber.objects.filter(cat_id=cat_id)
    if len(posts) == 0:  # если нет ни одной категории, то гегерируем ошибку
        raise Http404()

    posts = Barber.objects.filter(cat_id=cat_id) # в Barber берем только поле cat_id
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'cat_selected': cat_id
    }
    return render(request, 'barber/index.html', context=context)
    #return HttpResponse(f'<h2>Это страница категорий c id ={cat_id}</h2>')

# def category(request, catid):
#     return HttpResponse(f'<h2>Это страница категорий</h2>{catid}</p>')

# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)                        #raise Http404
#     # if request.GET:
#     #     print(request.GET)
#     return HttpResponse(f'<h2>Это страница архива</h2>{year}</p>')


def  pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2>Этa страница не найдена</h2>')
