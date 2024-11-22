import allure
from allure_commons.types import Severity

from pages.authorization_page import AuthorizationPage


@allure.title("Проверка title страницы авторизации")
@allure.severity(Severity.MINOR)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы авторизации")
@allure.parent_suite("Тесты UI")
def test_authorization_page_title(browser):
    authorization_page = AuthorizationPage(browser)
    authorization_page.open_authorization_page()

    authorization_page.verify_page_title()


@allure.title("Проверка элементов страницы авторизации")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы авторизации")
@allure.parent_suite("Тесты UI")
def test_authorization_page_elements(browser):
    authorization_page = AuthorizationPage(browser)
    authorization_page.open_authorization_page()

    authorization_page.verify_login_logo()
    authorization_page.verify_username_field()
    authorization_page.verify_password_field()
    authorization_page.verify_login_button()
