from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'services'
urlpatterns = [
    path('' , home , name = 'services')
]
