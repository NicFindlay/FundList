from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main():

    chromedriver = "/Users/nic/Documents/Django/FundList.co.za/chromedriver"
    option = webdriver.ChromeOptions()
    option.binary_location = (
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    )
    s = Service(chromedriver)
    driver = webdriver.Chrome(service=s, options=option)
    driver.get("https://www.bcis.co.za/boutique-collective-investments/funds/funds")

    all_data = {}
    factsheet = driver.find_elements(By.TAG_NAME, "a")
    for doc in factsheet:
        text = doc.get_attribute("innerHTML")
        href = doc.get_attribute("href")
        all_data[text] = href

    print(all_data)

    # links = []
    # factsheet = driver.find_elements(By.TAG_NAME, "tr")
    # for doc in factsheet:
    #     col = driver.find_elements(By.TAG_NAME, "td")
    #     for i in range(len(col)):
    #         print(col[i].text)

    # tables = driver.find_elements(By.XPATH, "//table/tbody/tr/td")
    # for row in tables:
    #     print(row[0])

    # table = driver.find_element(By.TAG_NAME, "table")
    # rows = table.find_elements(By.TAG_NAME, "tr")
    # for row in rows:
    #     if row.find_elements(By.TAG_NAME, "td") == []:
    #         continue
    #     else:
    #         print(row.find_elements(By.TAG_NAME, "td"))[0]
    #         fund_name = row.find_elements(By.TAG_NAME, "td")[0]
    #         date = row.find_elements(By.TAG_NAME, "td")[1].get_attribute()
    #         factsheet_link = row.find_elements(By.TAG_NAME, "td")[4].get_attribute(
    #             "href"
    #         )
    #         print(fund_name)
    #         print(date)
    #         print(factsheet_link)


if __name__ == "__main__":
    main()
