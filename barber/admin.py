from django.contrib import admin

from barber.models import *

class BarberAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') #выводим в админке поля из вкобок
    list_display_links = ('id', 'title') #указываем поля, которые будут ссылками
    search_fields = ('title', 'content') # по полям в скобках можем искать записи
admin.site.register(Barber, BarberAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
