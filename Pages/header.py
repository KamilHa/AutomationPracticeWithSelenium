from selenium.webdriver.common.by import By


class AccountInfo:
    CONTACT_US = (By.ID, "contact-link")
    SIGN_IN = (By.CLASS_NAME, "login")
    SIGN_OUT = (By.CLASS_NAME, "logout")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "a > span")

    def __init__(self, browser):
        self.browser = browser

    def check_if_the_user_is_logged(self, user):
        user_info = self.browser.find_element(*self.ACCOUNT_NAME)
        uss = user.get("v_first_name") + " " + user.get("v_last_name")
        return True if user_info.text.equals(uss) else False


