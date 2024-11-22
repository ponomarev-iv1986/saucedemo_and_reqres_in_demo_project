import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthorizationPage(BasePage):
    LOGIN_LOGO = By.CSS_SELECTOR, ".login_logo"
    USERNAME_FIELD = By.CSS_SELECTOR, "#user-name"
    PASSWORD_FIELD = By.CSS_SELECTOR, "#password"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#login-button"

    # ACTIONS
    @allure.step("Открытие страницы авторизации")
    def open_authorization_page(self) -> None:
        self.open_page("/")

    @allure.step("Ввод имени {value}")
    def fill_username(self, value: str) -> None:
        self.type_text_into_element(self.USERNAME_FIELD, value)

    def fill_password(self, value: str) -> None:
        with allure.step("Ввод пароля"):
            self.type_text_into_element(self.PASSWORD_FIELD, value)

    @allure.step("Нажатие кнопки подтверждения")
    def submit(self) -> None:
        self.click_on_element(self.LOGIN_BUTTON)

    # VERIFICATIONS
    @allure.step("Проверка title страницы")
    def verify_page_title(self) -> None:
        self.assert_that_page_have_title("Swag Labs")

    @allure.step("Проверка логотипа")
    def verify_login_logo(self) -> None:
        self.assert_that_element_is_visible(self.LOGIN_LOGO)

    @allure.step("Проверка наличия поля username")
    def verify_username_field(self) -> None:
        self.assert_that_element_is_visible(self.USERNAME_FIELD)

    @allure.step("Проверка наличия поля password")
    def verify_password_field(self) -> None:
        self.assert_that_element_is_visible(self.PASSWORD_FIELD)

    @allure.step("Проверка наличия кнопки подтверждения")
    def verify_login_button(self) -> None:
        self.assert_that_element_is_visible(self.LOGIN_BUTTON)
