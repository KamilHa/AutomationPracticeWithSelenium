import pytest

from Pages.create_an_account import CreateAccountByPuttingEmail
from Pages.put_personal_information import YourPersonalInformation
from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def test_basic_register(browser):
    User1 = {
        "v_first_name": "Kamil",
        "v_last_name" : "Hahaha",
        "v_email" : "kamil@hahaha.pl",
        "v_password" : "qwerty",
        "v_address" : "Zielna 123",
        "v_city" : "Wroclaw",
        "v_postal" : "12555",
        "v_country" : "United States",
        "v_mobile_phone" : "89837484783",
        "v_alias" : "My Address 1"

    }
    create_an_account_page = CreateAccountByPuttingEmail(browser)
    create_an_account_page.load()
    create_an_account_page.register(User1.get("v_email"))



    put_personal_information_page = YourPersonalInformation(browser)
    put_personal_information_page.pub_basic_information(User1)


