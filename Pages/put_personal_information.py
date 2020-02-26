from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class YourPersonalInformation:
    # Your personal information
    GENDER_MR = (By.ID, 'id_gender1')
    GENDER_MRS = (By.ID, 'id_gender2')
    FIRST_NAME = (By.ID, 'customer_firstname')
    LAST_NAME = (By.ID, 'customer_lastname')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    DAY_OF_BIRTH = (By.ID, 'days')
    MONTH_OF_BIRTH = (By.ID, 'months')
    YEAR_OF_BIRTH = (By.ID, 'years')

    #checkboxes
    NEWSLETTER = (By.ID, "newsletter")
    SPECIAL_OFFERS = (By.ID, "optin")

    # Your address
    FIRST_NAME_ADDRESS = (By.ID, 'firstname')
    LAST_NAME_ADDRESS = (By.ID, 'lastname')
    COMPANY = (By.ID, 'company')
    ADDRESS = (By.ID, 'address1')
    ADDRESS_LINE2 = (By.ID, 'address2')
    CITY = (By.ID, 'city')
    STATE = (By.ID, 'id_state')
    POSTCODE = (By.ID, 'postcode')
    COUNTRY = (By.ID, 'id_country')
    ADDITIONAL_INFO = (By.ID, 'other')
    HOME_PHONE = (By.ID, 'phone')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    ALIAS = (By.ID, 'alias')

    REGISTER_BUTTON = (By.ID, 'submitAccount')

    def __init__(self, browser):
        self.browser = browser

    def add_basic_information(self, user):
        if user.get("v_gender") == 1:
            gender = self.browser.find_element(*self.GENDER_MR).click()
        elif user.get("v_gender") == 2:
            gender = self.browser.find_element(*self.GENDER_MRS).click()

        first_name = self.browser.find_element(*self.FIRST_NAME).send_keys(user.get("v_first_name"))
        last_name = self.browser.find_element(*self.LAST_NAME).send_keys(user.get("v_last_name"))
        password = self.browser.find_element(*self.PASSWORD).send_keys(user.get("v_password"))

        if user.get("v_day"): Select(self.browser.find_element(*self.DAY_OF_BIRTH)).select_by_value(user.get("v_day"))
        if user.get("v_month"): Select(self.browser.find_element(*self.MONTH_OF_BIRTH)).select_by_value(user.get("v_month"))
        if user.get("v_year"): Select(self.browser.find_element(*self.YEAR_OF_BIRTH)).select_by_value(user.get("v_year"))

        if user.get("v_newsletter"): Select(self.browser.find_element(*self.NEWSLETTER)).click()
        if user.get("v_special_offers"): Select(self.browser.find_element(*self.SPECIAL_OFFERS)).click()
        address = self.browser.find_element(*self.ADDRESS).send_keys(user.get("v_address"))
        if user.get("v_address_line2"): Select(self.browser.find_element(*self.ADDRESS_LINE2)).send_keys(user.get("v_address_line2"))
        city = self.browser.find_element(*self.CITY).send_keys(user.get("v_city"))
        mobile = self.browser.find_element(*self.MOBILE_PHONE).send_keys(user.get("v_mobile_phone"))


        #if Coutry == United States than addidional fields are available: State, Zip/Postal Code
        country = Select(self.browser.find_element(*self.COUNTRY)).select_by_value(user.get("v_country"))
        if user.get("v_country") == "21":
            postcode = self.browser.find_element(*self.POSTCODE).send_keys(user.get("v_postal"))
            state = Select(self.browser.find_element(*self.STATE)).select_by_value(user.get("v_state"))


        register = self.browser.find_element(*self.REGISTER_BUTTON).submit()
