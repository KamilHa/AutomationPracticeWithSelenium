from selenium.webdriver.common.by import By


class AccountInfo:
    CONTACT_US = (By.ID, "contact-link")
    SIGN_IN = (By.CLASS_NAME, "login")
    SIGN_OUT = (By.CLASS_NAME, "logout")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "a > span")

    def __init__(self, browser):
        self.browser = browser

    def check_if_the_user_is_logged(self):
        # need to find a better way to return the right status
        try:
            login_status = self.browser.find_element(*self.SIGN_OUT)
        except:
            print("User is not logged")
            login_status = False

        return login_status

    def log_out(self):
        logout = self.browser.find_element(*self.SIGN_OUT)
        logout.click()
