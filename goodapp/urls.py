from django.contrib import admin
from django.urls import path, re_path, include

from goodapp import views

urlpatterns = [
    path('', views.Indexview.as_view()),
    # 不同种类
    re_path(r'^category/(?P<cid>\d+)$', views.Indexview.as_view()),
    # 分页信息
    re_path(r'^category/(?P<cid>\d+)/page/(?P<num>\d+)$', views.Indexview.as_view()),
    # 货物详情页面
    re_path(r'^gooddetails/(?P<goodsid>\d+)$', views.Detailview.as_view()),
    # 关于
    path('about/', views.aboutview),
]