import allure
from allure_commons.types import Severity

from pages.cart_page import CartPage
from pages.home_page import HomePage


@allure.title("Проверка URL страницы корзины")
@allure.severity(Severity.NORMAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы корзины")
@allure.parent_suite("Тесты UI")
def test_cart_page_url(browser, log_in_saucedemo, go_to_cart_saucedemo):
    cart_page = CartPage(browser)

    cart_page.verify_page_url()


@allure.title("Проверка title страницы корзины")
@allure.severity(Severity.MINOR)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы корзины")
@allure.parent_suite("Тесты UI")
def test_cart_page_title(browser, log_in_saucedemo, go_to_cart_saucedemo):
    cart_page = CartPage(browser)

    cart_page.verify_page_title()


@allure.title("Проверка элементов страницы корзины")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы корзины")
@allure.parent_suite("Тесты UI")
def test_cart_page_elements(browser, log_in_saucedemo, go_to_cart_saucedemo):
    cart_page = CartPage(browser)

    cart_page.verify_app_logo()
    cart_page.verify_shopping_cart_link()
    cart_page.verify_secondary_header()
    cart_page.verify_cart_list()
    cart_page.verify_continue_shopping_button()
    cart_page.verify_checkout_button()
    cart_page.verify_footer()


@allure.title("Проверка добавленных элементов в корзине")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Проверка страницы корзины")
@allure.parent_suite("Тесты UI")
def test_add_to_shopping_cart(browser, log_in_saucedemo):
    home_page = HomePage(browser)
    cart_page = CartPage(browser)

    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Backpack")
    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Bolt T-Shirt")
    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Onesie")
    home_page.click_on_shopping_cart_link()

    cart_page.verify_count_of_inventory_items(3)
