from django.contrib import admin
from django.urls import path, re_path, include

from userapp import views

urlpatterns = [
    # 注册、用户中心、登录
    path('register/', views.Registerview.as_view()),
    path('main/', views.Mainview.as_view()),
    path('login/', views.Loginview.as_view()),
    path('address/', views.Addressview.as_view()),
    path('loadaddr/', views.loadaddr),
    re_path(r'^deleteaddr/(?P<addrobjid>\d+)$', views.deleteaddr),

]