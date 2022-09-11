import math

from django.db import models

# Create your models here.
from goodapp.models import Color,Goods,Size
from userapp.models import Userinfo


class Cartitem(models.Model):
    goodsid=models.PositiveIntegerField()
    colorid=models.PositiveIntegerField()
    sizeid=models.PositiveIntegerField()
    count=models.PositiveIntegerField()
    isdelete=models.BooleanField(default=False)
    user=models.ForeignKey(Userinfo,on_delete=models.CASCADE)

    # 通过id获取其他模型
    def getcolor(self):
        return Color.objects.get(id=self.colorid)

    def getgoods(self):
        return Goods.objects.get(id=self.goodsid)

    def getsize(self):
        return Size.objects.get(id=self.sizeid)

    def gettotalprice(self):

        return math.ceil(int(self.count)*self.getgoods().price)


