#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from selenium import webdriver


def main():
    """Run administrative tasks."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fundlist.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def extraction():
    DRIVER_PATH = "/Users/nic/Documents/Django/FundList.co.za/chromedriver"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://google.com")


if __name__ == "__main__":
    main()
