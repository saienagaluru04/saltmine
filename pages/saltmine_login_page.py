from selenium.webdriver.common.by import By

class LoginPage:

    # Locators for identifying the input fields
    def __init__(self,driver):
        self.driver = driver
        self.email_textbox     = (By.XPATH,"//*[@id='email']")
        self.button            = (By.XPATH,"//span[@class='MuiButton-label']")
        self.password_textbox  = (By.XPATH,"//input[@id='password']")
        self.clicklogin        = (By.XPATH,"//span[contains(text(),'Login')]")
        self.newversionclick   = (By.XPATH,"//span[@class='MuiTypography-root MuiTypography-button sc-bdfCDU eKhMAg css-1r2t6z7']")
        self.clicksettings     = (By.XPATH,"//div[contains(text(),'QA')]")
        self.dropdown          = (By.XPATH,"//div[@class='sc-jrAGKZ kZykDB MuiBox-root css-1a9getn']")
        self.crossbutton       = (By.XPATH,"//*[@id='default-autocomplete']/div/div/div/div/button")
        self.customer_name     = (By.XPATH,"//input[@placeholder='Pick an option']")

# Methods which will be called by object reference in tests file
    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)
    
    def continue_button(self):
        self.driver.find_element(*self.button).click()

    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.clicklogin).click()

    def new_version_click(self):
        self.driver.find_element(*self.newversionclick).click()

    def click_settings(self):
        self.driver.find_element(*self.clicksettings).click()

    def dropdown_button(self):
        self.driver.find_element(*self.dropdown).click()
    
    def cross_button(self):
        self.driver.find_element(*self.crossbutton).click()

    def enter_customer_name(self,customername):
        self.driver.find_element(*self.customer_name).send_keys(customername)

