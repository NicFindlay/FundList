from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import PyPDF2
import urllib.request
import PyPDF2
import io
import pdfplumber
import re


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

            keywords = ["Portfolio Value: R"]

            with pdfplumber.open(remote_file_bytes) as pdf:
                pdf_text = pdf.pages[0].extract_text()
                for keyword in keywords:
                    before_keyword, text, after_keyword = pdf_text.partition(keyword)
                    market_cap = (after_keyword.split("\n")[0]).replace(" ", "")
                    print("Portfolio Value: R" + market_cap)


if __name__ == "__main__":
    # get_factsheets()
    extract_factsheets()
