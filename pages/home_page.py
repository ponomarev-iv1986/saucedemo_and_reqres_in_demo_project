import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    APP_LOGO = By.CSS_SELECTOR, ".app_logo"
    SHOPPING_CART_LINK = By.CSS_SELECTOR, "[data-test=shopping-cart-link]"
    SECONDARY_HEADER = By.CSS_SELECTOR, "[data-test=secondary-header]"
    INVENTORY_LIST = By.CSS_SELECTOR, "[data-test=inventory-list]"
    FOOTER = By.CSS_SELECTOR, "[data-test=footer]"
    SHOPPING_CART_BADGE = By.CSS_SELECTOR, "[data-test=shopping-cart-badge]"
    _INVENTORY_ITEM_LABEL = (
        By.XPATH,
        (
            "//*[contains(concat(' ', normalize-space(@class), ' '), "
            "' inventory_item_label ')]"
        ),
    )

    # ACTIONS
    @allure.step("Добавление в корзину товара {text}")
    def add_product_to_shopping_cart_by_text(self, text: str) -> None:
        product_locator = (
            By.XPATH,
            (
                self._INVENTORY_ITEM_LABEL[1]
                + f"[contains(.//text(), '{text}')]"
                + "/following-sibling::*/*[contains(text(), 'Add to cart')]"
            ),
        )
        self.click_on_element(product_locator)

    @allure.step("Нажатие на ссылку корзины")
    def click_on_shopping_cart_link(self) -> None:
        self.click_on_element(self.SHOPPING_CART_LINK)

    # VERIFICATION
    @allure.step("Проверка URL страницы")
    def verify_url(self) -> None:
        self.assert_that_url_contains("inventory")

    @allure.step("Проверка title страницы")
    def verify_page_title(self) -> None:
        self.assert_that_page_have_title("Swag Labs")

    @allure.step("Проверка логотипа страницы")
    def verify_app_logo(self) -> None:
        self.assert_that_element_have_text(self.APP_LOGO, "Swag Labs")

    @allure.step("Проверка наличия ссылки на корзину")
    def verify_shopping_cart_link(self) -> None:
        self.assert_that_element_is_visible(self.SHOPPING_CART_LINK)

    @allure.step("Проверка второго заголовка")
    def verify_secondary_header(self) -> None:
        self.assert_that_element_have_text(self.SECONDARY_HEADER, "Products")

    @allure.step("Проверка наличия списка товаров")
    def verify_inventory_list(self) -> None:
        self.assert_that_element_is_visible(self.INVENTORY_LIST)

    @allure.step("Проверка наличия футера")
    def verify_footer(self) -> None:
        self.assert_that_element_is_visible(self.FOOTER)

    @allure.step("Проверка значка количества добавленного товара в корзину")
    def verify_cart_badge_text(self, text: str) -> None:
        self.assert_that_element_have_text(self.SHOPPING_CART_BADGE, text)
