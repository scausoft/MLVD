import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.
class LightGBM(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.TextField(max_length=288) #
    contractType = models.CharField(max_length=32,default=0) #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)

class SmoteNN(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.TextField(max_length=288) #
    lType = models.CharField(max_length=32,default=0) #
    rType = models.CharField(max_length=32,default=0)  #
    xType = models.CharField(max_length=32,default=0)  #
    aType = models.CharField(max_length=32,default=0)  #
    sType = models.CharField(max_length=32,default=0)  #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)
class SmoteTT(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.TextField(max_length=288) #
    lType = models.CharField(max_length=32,default=0) #
    rType = models.CharField(max_length=32,default=0)  #
    xType = models.CharField(max_length=32,default=0)  #
    aType = models.CharField(max_length=32,default=0)  #
    sType = models.CharField(max_length=32,default=0)  #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)
class Smote(models.Model):
            id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
            contractName = models.CharField(max_length=32, default="默认值")  #
            byteCodes = models.TextField(max_length=288)  #
            lType = models.CharField(max_length=32, default=0)  #
            rType = models.CharField(max_length=32, default=0)  #
            xType = models.CharField(max_length=32, default=0)  #
            aType = models.CharField(max_length=32, default=0)  #
            sType = models.CharField(max_length=32, default=0)  #
            create_time = models.CharField(max_length=32)

            class Meta:
                ordering = ('create_time',)
def to_dict(self):
            """重写model_to_dict()方法转字典"""
            from datetime import datetime

            opts = self._meta
            data = {}
            for f in opts.concrete_fields:
                value = f.value_from_object(self)
                if isinstance(value, datetime):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(f, models.FileField):
                    value = value.url if value else None
                data[f.name] = value
            return data

class RF(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.CharField(max_length=256) #
    contractType = models.CharField(max_length=32) #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)


class XGBoost(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.TextField(max_length=64) #
    contractType = models.CharField(max_length=32) #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)



class SVM(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32, default="默认值")  #
    byteCodes = models.CharField(max_length=64)  #
    contractType = models.CharField(max_length=32)  #
    create_time = models.CharField(max_length=32)

    class Meta:
        ordering = ('create_time',)

class AdaBoost(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    contractName = models.CharField(max_length=32,default="默认值")  #
    byteCodes = models.CharField(max_length=64) #
    contractType = models.CharField(max_length=32) #
    create_time = models.CharField(max_length=32)
    class Meta:
        ordering = ('create_time',)


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    username = models.CharField(max_length=25,unique=True)
    password = models.CharField(max_length=25)
    roles = models.ManyToManyField(to='Role')
    def __str__(self):
        return self.username



class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name='身份名称')
    # 和权限表的多对多关系字段，一个身份可以有多个权限，一个权限也可以被多个身份拥有
    permissions = models.ManyToManyField(to='Permission')

    def __str__(self):
        return self.title

# 创建权限表
class Permission(models.Model):
    name = models.CharField(max_length=32, verbose_name='权限名称')
    url = models.CharField(max_length=32, verbose_name='权限url')

    def __str__(self):
        return self.name
