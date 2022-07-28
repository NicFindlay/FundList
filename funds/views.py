from django.shortcuts import render
from .models import Fund, Company, PriceData

# Create your views here.


def get_funds(request):
    fund_list = Fund.objects.order_by("id")
    company_list = Company.objects.order_by("id")
    price_list = PriceData.objects.order_by("id")
    context = {"fund_list": fund_list, "company_list": company_list}

    return render(request, "dashboard.html", context)
