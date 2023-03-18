from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from barber.views import pageNotFound
from djangoLesson import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('barber.urls'))
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
