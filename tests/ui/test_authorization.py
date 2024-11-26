import allure
from allure_commons.types import Severity

from config import settings
from pages.authorization_page import AuthorizationPage
from pages.home_page import HomePage


@allure.title("Проверка авторизации")
@allure.severity(Severity.BLOCKER)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка авторизации")
@allure.parent_suite("Тесты UI")
def test_authorization(browser):
    authorization_page = AuthorizationPage(browser)
    home_page = HomePage(browser)
    authorization_page.open_authorization_page()

    authorization_page.fill_username(settings.SAUCEDEMO_LOGIN)
    authorization_page.fill_password(settings.SAUCEDEMO_PASSWORD)
    authorization_page.submit()

    home_page.verify_url()
