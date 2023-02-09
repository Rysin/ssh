from selenium import webdriver
import chromedriver_autoinstaller
import pytest


@pytest.mark.UI
def test_basic_selenium():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title


def test_login():
    pass
