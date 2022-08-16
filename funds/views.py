from django.shortcuts import render
from .models import Fund, Company, PriceData

# Create your views here.


def get_funds(request):
    fund_list = Fund.objects.order_by("-market_cap")
    company_list = Company.objects.order_by("id")
    price_list = PriceData.objects.order_by("-date")
    # calculate_returns(fund_list, price_list)
    context = {
        "fund_list": fund_list,
        "company_list": company_list,
        "price_list": price_list,
    }

    return render(request, "dashboard.html", context)


def get_single_fund(request, fund):
    fund = fund.replace("-", " ")
    fund_object = Fund.objects.get(name=fund)

    # calculate_returns(fund_list, price_list)
    context = {
        "fund": fund_object,
    }
    return render(request, "single-fund.html", context)
