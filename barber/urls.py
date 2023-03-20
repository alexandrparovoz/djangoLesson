from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('cats/<int:catid>/', category, name='cats'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('archive/<int:year>/', archive, name='arcive')
]