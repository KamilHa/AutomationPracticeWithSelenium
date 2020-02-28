from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AccountInfo:
    CONTACT_US = (By.ID, "contact-link")
    SIGN_IN = (By.CLASS_NAME, "login")
    SIGN_OUT = (By.CLASS_NAME, "logout")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "a > span")

    def __init__(self, browser):
        self.browser = browser

    def check_if_the_user_is_logged(self):

        try:
            user_info = self.browser.find_element(*self.SIGN_OUT)
        except:
            print("User is not logged")
            user_info = False

        return True if user_info else False

    def log_out(self):
        logout = self.browser.find_element(*self.SIGN_OUT)
        logout.click()
