from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CreateAccountByPuttingEmail:
    URL = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'


    # Create an account
    EMAIL_TO_CREATE = (By.ID, 'email_create')
    BUTTON_TO_CREATE = (By.ID, 'SubmitCreate')

    # Already registered?
    EMAIL_TO_LOG_IN = (By.ID, 'email')
    PASSWORD_TO_LOG_IN = (By.ID, 'passwd')
    BUTTON_TO_LOG_IN = (By.ID, 'SubmitLogin')
    FORGOT_PASSWORD_LINK = (By.CLASS_NAME, 'lost_password form-group')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def register(self, email):
        email_input_to_create = self.browser.find_element(*self.EMAIL_TO_CREATE)
        email_input_to_create.send_keys(email)

        email_button_to_create = self.browser.find_element(*self.BUTTON_TO_CREATE)
        email_button_to_create.click()

    def log_in(self, user):
        email_input_to_create = self.browser.find_element(*self.EMAIL_TO_LOG_IN)
        email_input_to_create.send_keys(user.get("v_email"))

        email_input_to_create = self.browser.find_element(*self.PASSWORD_TO_LOG_IN)
        email_input_to_create.send_keys(user.get("v_password"))

        email_button_to_create = self.browser.find_element(*self.BUTTON_TO_LOG_IN)
        email_button_to_create.click()



