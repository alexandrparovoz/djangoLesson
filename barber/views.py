from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse(f'<h2>Это страница главная</h2>')#render(request, 'index.html')


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
