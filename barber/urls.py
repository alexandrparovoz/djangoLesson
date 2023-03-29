from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
   # path('contact/', contact, name='contact'),
    path('login/', Login.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]