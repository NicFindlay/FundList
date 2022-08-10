from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import django
import urllib.request
import io
import PyPDF2
from funds.models import Fund, PriceData


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
            try:
                pdfdoc_remote = PyPDF2.PdfFileReader(remote_file_bytes)
            except:
                print("An exception occurred")

            keywords = ["Value: R", "NAV Price as at month end:"]
            name = line[0]
            factsheet = line[1]
            market_cap = ""
            price = ""
            date = "30/06/2022"

            pdf_text = pdfdoc_remote.pages[0].extract_text()
            before_keyword, text, after_keyword = pdf_text.partition(keywords[0])
            market_cap = (after_keyword.split("\n")[0]).replace(" ", "")

            before_keyword, text, after_keyword = pdf_text.partition(keywords[1])
            price = (
                (after_keyword.split("\n")[0]).replace(" ", "").removesuffix("cents")
            )
            price = price.replace(",", "")

            print("Portfolio Value: R" + market_cap)
            print("Unit Price: " + price)

            insert_fund(name, price, market_cap)


# Calculate fund returns from Pricing and send to Fund DB
def insert_fund(fund_name):
    if Fund.objects.filter(name=fund_name):
        print("EXISTS")
        exit
    else:
        try:
            new_fund = Fund.objects.create(name=fund_name)
            new_fund.save()
        except:
            print("An exception occurred trying to add Fund")


def insert_price_data(fund_name, fund_price, fund_market_cap):
    if Fund.objects.filter(name=fund_name):
        exit
    else:
        try:
            new_fund = Fund.objects.create(
                name=fund_name, price=fund_price, market_cap=fund_market_cap
            )
            new_fund.save()
        except:
            print("An exception occurred trying to add Fund")


if __name__ == "__main__":
    # get_factsheets()
    extract_factsheets()
