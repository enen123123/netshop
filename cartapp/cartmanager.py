from collections import OrderedDict
from models import *
from django.db.models import F
# import jsonpickle
#
#
#
# class DBcartmanger(cartmanger):
#     def __init__(self):
#         self.user=user
#     def add(self,goodsid,colorid,sizeid,count,*args,**kwargs) :
#         if self.user.cartitem_set.filter(goodsid=goodsid,colorid=colorid,sizeid=sizeid).count()==1:
#             self.update(goodsid,colorid,sizeid,count,*args,**kwargs)
#         else:
#             CartItem.objects.create(goodsid=goodsid,colorid=colorid,sizeid=sizeid,count=count,user=




# 工厂方法
# 根据当前用户是否登录返回相应的CartManger对象
# def getcartmanger(reguest):
#     if request.session.get('user'):
#     #当前用户已登录
#         return DBcartmanger(request.session.get('user'))
#     return sessioncartmanager(request.session)



