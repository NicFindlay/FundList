from __future__ import unicode_literals
from telnetlib import LOGOUT
from django.db import models
from django.utils import timezone

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)  # PK
    logo = models.FileField(upload_to="static/images/funds/")
    website = models.URLField(blank=True)

    funds_managed = models.ManyToManyField("Fund", verbose_name="List of funds")

    def __str__(self):
        return self.name


class Fund(models.Model):
    company_link = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    factsheet = models.URLField(blank=True)

    pricing_data = models.ManyToManyField("PriceData", verbose_name="Pricing Data")

    def __str__(self):
        return self.name


class PriceData(models.Model):
    fund_link = models.ForeignKey(Fund, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    price = models.BigIntegerField()
    marketcap = models.BigIntegerField()

    def __str__(self):
        return str(self.date)
