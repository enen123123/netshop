from django.contrib import admin
from django.urls import path, re_path, include

from orderapp import views

urlpatterns = [
    path('', views.orderview),


]

