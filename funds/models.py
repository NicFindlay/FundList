from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.


class Fund(models.Model):
    """
    The Generic Fund Class
    """

    name = models.CharField(max_length=250, primary_key=True, unique=True)
    manager = models.CharField(max_length=250)
    marketcap = models.CharField(max_length=250)

    def __str__(self):
        return self
