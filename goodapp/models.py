import collections

from django.db import models

# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=10)
    def __unicode__(self):
        return u'<Category:s%>'%self.cname

class Goods(models.Model):
    gname=models.CharField(max_length=100,unique=True)
    gdesc=models.CharField(max_length=100)
    oldprice=models.DecimalField(max_digits=6,decimal_places=2)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __unicode__(self):
        return u'<Goods:s%>'%self.gname
    def getcolorimg(self):
        # 通过颜色获取第一个衣服的图片地址
        return self.inventory_set.first().color.colorurl
    def getcolor(self):
        # 获取所有颜色衣服的图片地址
        colors=[]
        for inventory in self.inventory_set.all():
            if inventory.color not in colors:
                colors.append(inventory.color)
        return colors
    def getsize(self):
        # 获取所有尺码
        size=[]
        for inventory in self.inventory_set.all():
            if inventory.color not in size:
                size.append(inventory.size)
        return size

    def getdetailfoot(self):
        # 展示商品规格
        # 采用了以时间为顺序字典模块
        dfoot = collections.OrderedDict()

        # 遍历所有详细信息
        for detail in self.gooddeatil_set.all():
            # 获取参数规格等
            gdname=detail.getname()
            # 判断当前详细信息是否存在
            # Python2有has_key()方法,Python3以后删除了has_key()方法！
            # Python3方法更改为：if key1 in adict:
            # if not dfoot.has_key(gdname):
            if not gdname in dfoot:
                dfoot[gdname]=[detail.gdurl]
            else:
                dfoot[gdname].append(detail.gdurl)
        return dfoot

# 可以用以下格式，在console控制台更改数据库内容
# from goodsapp.models import*
# GoodDetail.objects.filter(goodsdname__gdname=u'参数规格" ).update(gdurl='/static/10.png')


class Gooddeatilname(models.Model):
    gdname=models.CharField(max_length=30)


class Gooddeatil(models.Model):
    # 空即为默认的media下图片
    #  Pillow安装模块
    gdurl=models.ImageField(upload_to='')
    goodsdname=models.ForeignKey(Gooddeatilname,on_delete=models.CASCADE)
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE)

    def getname(self):
        # 通过商品详细表获取详细名字
        return self.goodsdname.gdname

class Size(models.Model):
    sname=models.CharField(max_length=10)

class Color(models.Model):
    colorname=models.CharField(max_length=10)
    # 每个图片的颜色
    colorurl=models.ImageField(upload_to='color/')

# 库存
class Inventory(models.Model):
    # 正整数PositiveIntegerField
    count=models.PositiveIntegerField(default=100)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)

# mysqlclient  mysql数据库所需模块

