from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<int:catid>/', category, name='cats'),
    path('archive/<int:year>/', archive, name='arcive')
]