# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# python manage.py inspectdb>userapp/models.py
# 在Terminal上键入以上信息，既可以将mysql数据库中数据模型整理到指定位置


class Area(models.Model):
    areaid = models.IntegerField(primary_key=True)
    areaname = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(blank=True, null=True)
    arealevel = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # 不会被牵引文件到数据库重新建立一个表
        managed = False
        db_table = 'area'

class Userinfo(models.Model):
    uname=models.EmailField()
    pwd=models.CharField(max_length=16)

    class Meta:
        # 排序,必须元组形式
        ordering=('id',)

class Address(models.Model):
    aname=models.CharField(max_length=255)
    aphone=models.CharField(max_length=255)
    addr=models.CharField(max_length=255)
    isdefault=models.BooleanField(default=False)
    userinfo=models.ForeignKey(Userinfo,on_delete=models.CASCADE)

