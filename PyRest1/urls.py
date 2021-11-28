
from django.contrib import admin
from django.urls import path, include
from restapp1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restapp1.urls')),
]
