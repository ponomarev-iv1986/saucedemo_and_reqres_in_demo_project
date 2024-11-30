import allure
from allure_commons.types import Severity

from pages.cart_page import CartPage
from pages.home_page import HomePage


@allure.title("Проверка покупки продукта")
@allure.severity(Severity.CRITICAL)
@allure.tag("UI", "REGRESS")
@allure.suite("Сквозные позитивные тесты")
@allure.parent_suite("Тесты UI")
def test_buy_to_product(browser, log_in_saucedemo):
    home_page = HomePage(browser)
    cart_page = CartPage(browser)

    home_page.add_product_to_shopping_cart_by_text("Sauce Labs Fleece Jacket")
    home_page.click_on_shopping_cart_link()
    cart_page.click_checkout_button()
    cart_page.fill_first_name("Bob")
    cart_page.fill_last_name("Beard")
    cart_page.fill_postal_code("12345")
    cart_page.click_continue_button()
    cart_page.click_finish_button()

    cart_page.verify_complete_header()
