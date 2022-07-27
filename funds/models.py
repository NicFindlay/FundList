from __future__ import unicode_literals
from telnetlib import LOGOUT
from django.db import models
from django.utils import timezone

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250, primary_key=True, unique=True)  # PK
    logo = models.URLField(blank=True)
    marketcap = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Fund(models.Model):
    id = models.AutoField(primary_key=True, default=43)  # PK
    company_id = models.ManyToManyField(Company, blank=True)  # FK
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class PriceData(models.Model):
    id = models.AutoField(primary_key=True, default=22)  # PK
    fund_id = models.ForeignKey(Fund, on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now)
    price = models.BigIntegerField()
    marketcap = models.CharField(max_length=250)
