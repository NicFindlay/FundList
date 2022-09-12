from funds.models import Fund, Company, PriceData


def calculate():
    fund_list = Fund.objects.order_by("-market_cap")
    price_list = PriceData.objects.order_by("-date")
    calculate_charts()


def remove_spam_from_name(name):
    return name.split("(A)", 1)[0]


def calculate_charts():
    fund_list = Fund.objects.order_by("-market_cap")
    for fund in fund_list:
        print("Calculating returns " + fund.name)
        pricequery = PriceData.objects.filter(fund_link=fund.id).order_by("-date")
        chart = []
        count = 0
        for price in pricequery:
            if count < 10:
                chart.append(price.price)
                count = count + 1
            else:
                break
        print(chart)
        fund.chart = chart
        fund.save()


# Calculate fund returns from Pricing and send to Fund DB
def calculate_returns(fund_list, price_list):
    for fund in fund_list:
        print("Calculating returns " + fund.name)
        # local_price_list = []

        # for price in price_list:
        #     if price.fund_link == fund:
        #         local_price_list.append(price)

        pricequery = PriceData.objects.filter(fund_link=fund.id).order_by("-date")

        if len(pricequery) > 0:
            latest_price = pricequery[0].price
            # shares = local_price_list[0].shares
            # marketcap = local_price_list[0].market_cap

            # fund.market_cap = marketcap
            # fund.shares = shares
            fund.price = latest_price
            # shares_vs_marketcap(fund, shares, marketcap, latest_price)

        if len(pricequery) > 1:
            last_price = pricequery[1].price
            # print(str(last_price) + " | " + str(latest_price))
            fund.one_month = round(((latest_price - last_price) / last_price) * 100, 2)

        if len(pricequery) > 5:
            six_price = pricequery[5].price
            fund.six_month = round(((latest_price - six_price) / six_price) * 100, 2)

        if len(pricequery) > 11:
            year_price = pricequery[11].price
            # print(str(year_price) + " | " + str(latest_price))
            fund.one_year = round(((latest_price - year_price) / year_price) * 100, 2)

        fund.save()


def shares_vs_marketcap(_fund, _shares, _marketcap, _latest_price):
    if _shares:
        _fund.market_cap = _latest_price * _shares
        # print("Updates MC " + _fund.name)
    elif _marketcap:
        _fund.shares = _marketcap / _latest_price
        # print("Updates SHARES " + str(_marketcap / _latest_price) + _fund.name)
    else:
        print("No shares or marketcap found")
    _fund.save()
