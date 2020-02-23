from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YourPersonalInformation:

    #Your personal information
    GENDER_MR = (By.ID, 'id_gender1')
    GENDER_MRS = (By.ID, 'id_gender2')
    FIRST_NAME = (By.ID, 'customer_firstname')
    LAST_NAME = (By.ID, 'customer_lastname')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')

    #Your addressYour address
    FIRST_NAME_ADDRESS = (By.ID, 'firstname')
    LAST_NAME_ADDRESS = (By.ID, 'lastname')
    COMPANY = (By.ID, 'company')
    ADDRESS = (By.ID, 'address1')
    ADDRESS_LINE2 = (By.ID, 'address2')
    CITY = (By.ID, 'city')
    STATE = (By.ID, 'id_state')
    POSTCODE = (By.ID, 'postcode')
    COUNTRY_SELECTOR = (By.ID, 'id_country')
    ADDITIONAL_INFO = (By.ID, 'other')
    HOME_PHONE = (By.ID, 'phone')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    ALLIAS = (By.ID, 'alias')

    REGISTER_BUTTON = (By.ID, 'submitAccount')



    def __init__(self, browser):
        self.browser = browser

    def pub_basic_information(self, user):
        first_name = self.browser.find_element(*self.FIRST_NAME).send_keys(user.get("v_first_name"))
        last_name = self.browser.find_element(*self.LAST_NAME).send_keys(user.get("v_last_name"))
        password = self.browser.find_element(*self.PASSWORD).send_keys(user.get("v_password"))
        address = self.browser.find_element(*self.CITY).send_keys(user.get("v_city"))
        city = self.browser.find_element(*self.ADDRESS).send_keys(user.get("v_address"))
        postcode = self.browser.find_element(*self.POSTCODE).send_keys(user.get("v_postal"))
        mobile = self.browser.find_element(*self.MOBILE_PHONE).send_keys(user.get("v_mobile_phone"))

        register = self.browser.find_element(*self.REGISTER_BUTTON).submit()



