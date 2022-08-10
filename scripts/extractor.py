from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import django
import urllib.request
import io
import pdfplumber
from funds.models import Fund


all_data = {}


def get_factsheets():

    chromedriver = "/Users/nic/Documents/Django/FundList.co.za/chromedriver"
    option = webdriver.ChromeOptions()
    option.binary_location = (
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    )
    s = Service(chromedriver)
    driver = webdriver.Chrome(service=s, options=option)
    driver.get("https://www.bcis.co.za/boutique-collective-investments/funds/funds")

    factsheet = driver.find_elements(By.TAG_NAME, "a")
    for doc in factsheet:
        text = doc.get_attribute("innerHTML")
        href = doc.get_attribute("href")
        if "https://www.bcis.co.za/upload/factsheet_categories_folders/" in str(href):
            all_data[text] = href

    with open("bci_factsheets.csv", "w") as f:
        for key in all_data.keys():
            f.write("%s,%s\n" % (key, all_data[key]))


def extract_factsheets():

    filename = "bci_factsheets.csv"
    with open(filename, "r") as data:
        for line in csv.reader(data):
            print(line[0])
            URL = line[1]
            req = urllib.request.Request(URL, headers={"User-Agent": "Magic Browser"})
            remote_file = urllib.request.urlopen(req).read()
            remote_file_bytes = io.BytesIO(remote_file)

            keywords = ["Portfolio Value: R", "NAV Price as at month end:"]
            name = line[0]
            factsheet = line[1]
            market_cap = ""
            price = ""
            shares = ""
            date = "30/06/2022"

            with pdfplumber.open(remote_file_bytes) as pdf:
                pdf_text = pdf.pages[0].extract_text()
                before_keyword, text, after_keyword = pdf_text.partition(keywords[0])
                market_cap = (after_keyword.split("\n")[0]).replace(" ", "")

                before_keyword, text, after_keyword = pdf_text.partition(keywords[1])
                price = (
                    (after_keyword.split("\n")[0])
                    .replace(" ", "")
                    .removesuffix("cents")
                )

                print("Portfolio Value: R" + market_cap)
                print("Unit Price: " + price)

            insert_fund("Allan Gray Balanced Fund", price, shares, market_cap, date)


# Calculate fund returns from Pricing and send to Fund DB
def insert_fund(fund_name, fund_price, fund_shares, fund_market_cap, date):
    if Fund.objects.filter(name=fund_name):
        print("EXISTS")

    # for fund in fund_list:
    #     local_price_list = []
    #     for price in price_list:
    #         if price.fund_link == fund:

    #             local_price_list.append(price)
    #             print(local_price_list[0])

    #     latest_price = local_price_list[0].price
    #     last_price = local_price_list[1].price
    #     shares = local_price_list[0].shares

    #     fund.shares = shares
    #     fund.market_cap = latest_price * shares
    #     fund.price = latest_price
    #     fund.one_month = round(((latest_price - last_price) / last_price) * 100, 2)
    #     if len(price_list) > 5:
    #         six_price = price_list[5].price
    #         fund.six_month = round(((latest_price - six_price) / six_price) * 100, 2)
    #     if len(price_list) > 11:
    #         year_price = price_list[11].price
    #         fund.one_year = round(((latest_price - year_price) / year_price) * 100, 2)

    #     fund.save()


if __name__ == "__main__":
    # get_factsheets()
    extract_factsheets()
