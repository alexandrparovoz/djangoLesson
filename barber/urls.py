from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', category, name='cats'),
    path('archive/<int:year>/', archive, name='arcive')
]