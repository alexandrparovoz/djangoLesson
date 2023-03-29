from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
    photo = forms.ImageField(label='Фото')
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')