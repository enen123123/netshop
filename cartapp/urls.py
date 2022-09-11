from django.contrib import admin
from django.urls import path, re_path, include

from cartapp import views

urlpatterns = [
    path('', views.Cartview.as_view()),
    path('queryall/', views.queryall),
    # 传递被删除的参数地址
    re_path(r'^deletequery/(?P<cartitemid>\d+)$', views.deletequery),

]