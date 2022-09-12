from django.shortcuts import render
from .models import Fund, Company, PriceData


# Create your views here.


def get_funds(request):
    fund_list = Fund.objects.order_by("-market_cap")
    monthly_winners = Fund.objects.order_by("-one_month")
    annual_winners = Fund.objects.order_by("-one_year")
    company_list = Company.objects.order_by("id")
    price_list = PriceData.objects.order_by("-date")
    context = {
        "fund_list": fund_list,
        "company_list": company_list,
        "price_list": price_list,
        "monthly_winners": monthly_winners,
        "annual_winners": annual_winners,
    }

    return render(request, "dashboard.html", context)


def get_single_fund(request, fund):
    fund = fund.replace("-", " ")
    fund_object = Fund.objects.get(name=fund)
    price_data = PriceData.objects.filter(fund_link=fund_object.id)
    chart_data = []

    for price in price_data:
        col = []
        col.append(price.date.strftime("%Y-%m"))
        col.append(price.price)
        chart_data.append(col)

    # calculate_returns(fund_list, price_list)
    context = {
        "fund": fund_object,
        "price_data": price_data,
        "chart_data": chart_data,
    }
    return render(request, "single-fund.html", context)


def search_funds(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        funds = Fund.objects.filter(name__contains=searched)

        return render(request, "search.html", {"searched": searched, "funds": funds})
    else:
        return render(request, "search.html")
