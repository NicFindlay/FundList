from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import PyPDF2
import urllib.request
import PyPDF2
import io


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
    # print(all_data)
    # link = all_data["BCI Best Blend Balanced Fund (C) BBBCF"]
    # print(link)

    URL = "https://www.bcis.co.za/upload/factsheet_categories_folders/funds/Harvard%20House%20Investment%20Management/Harvard%20House%20BCI%20Equity%20Fund%20(A)%20MHGE.pdf"
    req = urllib.request.Request(URL, headers={"User-Agent": "Magic Browser"})
    remote_file = urllib.request.urlopen(req).read()
    remote_file_bytes = io.BytesIO(remote_file)
    pdfdoc_remote = PyPDF2.PdfFileReader(remote_file_bytes)

    # extracting text from page
    print(pdfdoc_remote.getPage(0).extractText())


if __name__ == "__main__":
    # get_factsheets()
    extract_factsheets()
