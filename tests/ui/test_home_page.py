import allure
from allure_commons.types import Severity

from pages.home_page import HomePage


@allure.title("Проверка title домашней страницы")
@allure.severity(Severity.MINOR)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка домашней страницы")
@allure.parent_suite("Тесты UI")
def test_home_page_title(browser, log_in_saucedemo):
    home_page = HomePage(browser)

    home_page.verify_page_title()


@allure.title("Проверка элементов домашней страницы")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка домашней страницы")
@allure.parent_suite("Тесты UI")
def test_home_page_elements(browser, log_in_saucedemo):
    home_page = HomePage(browser)

    home_page.verify_app_logo()
    home_page.verify_shopping_cart_link()
    home_page.verify_secondary_header()
    home_page.verify_inventory_list()
    home_page.verify_footer()


@allure.title("Проверка добавления продуктов в корзину")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка домашней страницы")
@allure.parent_suite("Тесты UI")
def test_add_to_shopping_cart(browser, log_in_saucedemo):
    home_page = HomePage(browser)

    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Backpack")
    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Bolt T-Shirt")
    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Onesie")

    home_page.verify_cart_badge_text("3")
