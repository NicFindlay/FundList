from django.shortcuts import render
from .models import Fund, Company

# Create your views here.


def get_funds(request):
    fund_list = Fund.objects
    company_list = Company.objects

    context = {"fund_list": fund_list, "company_list": company_list}
    return render(request, "dashboard.html", context)
