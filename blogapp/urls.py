from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('like/<str:pk>',likeBlog,name='like'),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)