from selenium import webdriver


def main():
    DRIVER_PATH = "/Users/nic/Documents/Django/FundList.co.za/chromedriver"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://google.com")


if __name__ == "__main__":
    main()
