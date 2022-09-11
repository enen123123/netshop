from django.db import models

# Create your models here.
from userapp.models import Address,Userinfo


# class Order(models.Model):
#     # 另一种字符串
#     outtradenum=models.UUIDField()
#     ordernum=models.CharField(max_length=50)
#     tradeno=models.CharField(max_length=120,default='')
#     status=models.CharField(max_length=20,default='待支付')
#     payway=models.CharField(max_length=20,default='微信支付')
#
#     address=models.ForeignKey(Address,on_delete=models.CASCADE)
#     user=models.ForeignKey(Userinfo,on_delete=models.CASCADE)

# class Orderitem(models.Model):
#     goodsid=models.PositiveIntegerField
#     colorid = models.PositiveIntegerField
#     sized = models.PositiveIntegerField
#     count = models.PositiveIntegerField
#
#     order=models.ForeignKey(Order,on_delete=models.CASCADE)






