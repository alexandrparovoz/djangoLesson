from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404


from .models import *
from .forms import AddPostForm



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
    contact_list = Barber.objects.all()
    paginator = Paginator(contact_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'barber/about.html', {'page_obj': page_obj})


def addpage(request):
    if request.method == 'POST':  # если это пост запрос(юзер отправил данные)
        form = AddPostForm(request.POST, request.FILES) # то отдаeм их переменной form(заполненные)
        if form.is_valid():
            try:
                Barber.objects.create(**form.cleaned_data)# если все хорошо, то в БД запишутся данные  от юзера
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления данных')

    else:
        form = AddPostForm() # но если это первый показ формы(пусто) то и форма пуста
    return render(request, 'barber/addpage.html', {'form': form})


def contact(request):
    return HttpResponse("Обратная связь")

def registration(request):
    return HttpResponse("Регистрация")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    post = get_object_or_404(Barber, pk=post_id) # функция get_-- работает, если нет искомого id

    context = {
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'barber/post.html', context=context)

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


# def archive(request, year):
#     if int(year) > 2023:
#         return redirect('home', permanent=True)                        #raise Http404
#     # if request.GET:
#     #     print(request.GET)
#     return HttpResponse(f'<h2>Это страница архива</h2>{year}</p>')


def  pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2>Этa страница не найдена</h2>')
