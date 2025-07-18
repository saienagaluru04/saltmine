import pytest
from pages.saltmine_login_page import LoginPage

def test_saltmine_login(driver):  # ✅ driver comes from the conftest.py fixture
    driver.get("https://sit.saltmine.com")

    testlogin = LoginPage(driver)
    testlogin.enter_email("saltmineqa@gmail.com")
    testlogin.continue_button()
    testlogin.enter_password("QATest@2023")
    testlogin.click_login()
    testlogin.new_version_click()
    testlogin.click_settings()
    testlogin.dropdown_button()
    testlogin.cross_button()
    testlogin.enter_customer_name("AutoTest_DND")
