from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

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

# хотел потренироваться на этом представлении в пагинации
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


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'barber/register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрация")
    #     return dict(list(context.items()) + list(c_def.items()))


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'barber/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

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


class DeletePost(DeleteView):
    model = Barber
    template_name = 'barber/delete_post.html'

    def get_success_url(self):
        return reverse_lazy('home')


def  pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2>Этa страница не найдена</h2>')
