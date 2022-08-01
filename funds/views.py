from django.shortcuts import render
from .models import Fund, Company, PriceData

# Create your views here.


def get_funds(request):
    fund_list = Fund.objects.order_by("id")
    company_list = Company.objects.order_by("id")
    price_list = PriceData.objects.order_by("-date")
    calculate_returns(fund_list, price_list)
    context = {
        "fund_list": fund_list,
        "company_list": company_list,
        "price_list": price_list,
    }

    return render(request, "dashboard.html", context)


# Calculate fund returns from Pricing and send to Fund DB
def calculate_returns(fund_list, price_list):
    for fund in fund_list:
        local_price_list = []
        for price in price_list:
            if price.fund_link == fund:

                local_price_list.append(price)
                print(local_price_list[0])

        latest_price = local_price_list[0].price
        last_price = local_price_list[1].price
        shares = local_price_list[0].shares

        fund.shares = shares
        fund.market_cap = latest_price * shares
        fund.price = latest_price
        fund.one_month = round(((latest_price - last_price) / last_price) * 100, 2)
        if len(price_list) > 5:
            six_price = price_list[5].price
            fund.six_month = round(((latest_price - six_price) / six_price) * 100, 2)
        if len(price_list) > 11:
            year_price = price_list[11].price
            fund.one_year = round(((latest_price - year_price) / year_price) * 100, 2)

        fund.save()
