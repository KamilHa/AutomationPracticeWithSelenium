import pytest

from Pages.create_an_account import CreateAccountByPuttingEmail
from Pages.put_personal_information import YourPersonalInformation
from Pages.header import AccountInfo
from selenium.webdriver import Firefox

User1 = {
    "v_first_name": "Kamik",
    "v_last_name": "Hahahda",
    "v_email": "kamil@hdvajjhaha.pl",
    "v_password": "qwedrty",
    "v_address": "Zidelna 123",
    "v_city": "Wroclaw",
    "v_postal": "12555",
    "v_country": "21",
    "v_mobile_phone": "89837484783",
    "v_alias": "My Address 1d",
    "v_gender": 2,
    "v_day": "12",
    "v_month": "1",
    "v_year": "1972",
    "v_state": "3"
}

User2 = {"v_first_name": "Kamil", "v_last_name": "Testowy", "v_email": "kamil@o2.pl", "v_password": "secret22"}


@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def test_log_IN_log_OUT(browser, user = User2):
    create_an_account_page = CreateAccountByPuttingEmail(browser)
    create_an_account_page.load()

    create_a_header_page = AccountInfo(browser)

    # a user should not be logged in
    assert False == create_a_header_page.check_if_the_user_is_logged()

    # log in
    create_an_account_page.log_in(User2)

    # a user should be logged in
    assert True == create_a_header_page.check_if_the_user_is_logged()

    # log out
    create_a_header_page.log_out()

    # a user should be again logged out
    assert False == create_a_header_page.check_if_the_user_is_logged()


def test_basic_register(browser, user = User1):

    create_an_account_page = CreateAccountByPuttingEmail(browser)
    create_an_account_page.load()
    create_an_account_page.register(user.get("v_email"))

    put_personal_information_page = YourPersonalInformation(browser)
    put_personal_information_page.add_basic_information(user)



