from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.saltmine_login_page import LoginPage
import time

@given("I launch the browser")
def step_launch_browser(context):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@when("I open the Saltmine login page")
def step_open_login_page(context):
    context.driver.get("https://sit.saltmine.com")
    context.login_page = LoginPage(context.driver)

@when('I enter email "{email}"')
def step_enter_email(context, email):
    context.login_page.enter_email(email)

@when("I click the continue button")
def step_click_continue(context):
    context.login_page.continue_button()

@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@when("I click on the new version banner")
def step_click_new_version(context):
    context.login_page.new_version_click()

@when("I click on the QA settings")
def step_click_settings(context):
    context.login_page.click_settings()

@when("I open the dropdown")
def step_dropdown(context):
    context.login_page.dropdown_button()

@when("I click the cross button")
def step_cross_button(context):
    context.login_page.cross_button()

@when('I enter customer name "{name}"')
def step_enter_customer_name(context, name):
    context.login_page.enter_customer_name(name)

@then("I should be logged in successfully")
def step_verify_login(context):
    # Optional: add assertion or sleep for now
    time.sleep(2)
    assert "sit.saltmine.com" in context.driver.current_url
    context.driver.quit()
