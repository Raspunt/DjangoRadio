from django.contrib import admin
from django.urls import path, re_path
from . views import *




urlpatterns = [
    re_path(r'^',StartPage, name = "startPageUrl"),
]
