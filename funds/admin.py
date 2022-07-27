from django.contrib import admin
from .models import Company, Fund, PriceData

# Register your models here.

admin.site.register(Fund)
admin.site.register(Company)
admin.site.register(PriceData)
