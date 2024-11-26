from typing import Any, Type

import allure
from pydantic import BaseModel, ValidationError
from requests import Response

from config import settings
from http_clients.session import CustomSession


class ReqresInHttpClient:
    def __init__(self) -> None:
        self.request = CustomSession(settings.REQRES_IN_URL)

    # METHODS
    @allure.step("Получение списка пользователей")
    def list_users(self, page: int, per_page: int) -> Response:
        params = {
            "page": page,
            "per_page": per_page,
        }
        return self.request.get("/api/users", params=params)

    @allure.step("Получение пользователя с id = {user_id}")
    def retrieve_user(self, user_id: int) -> Response:
        return self.request.get(f"/api/users/{user_id}")

    @allure.step("Получение списка ресурсов")
    def list_resources(self, page: int, per_page: int) -> Response:
        params = {
            "page": page,
            "per_page": per_page,
        }
        return self.request.get("/api/resource", params=params)

    @allure.step("Получение ресурса с id = {resource_id}")
    def retrieve_resource(self, resource_id: int) -> Response:
        return self.request.get(f"/api/resource/{resource_id}")

    # ASSERTIONS
    @staticmethod
    @allure.step("Проверка, что статус код ответа равен {expected_status_code}")
    def assert_that_status_code_equal(
        response: Response,
        expected_status_code: int,
    ) -> None:
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, (
            "Неверный статус-код ответа.\n"
            f"Ожидался: {expected_status_code}.\nАктуальный: {actual_status_code}."
        )

    @staticmethod
    @allure.step("Валидация ответа по модели {model}")
    def validate_model(body: dict[str, Any], model: Type[BaseModel]) -> None:
        try:
            model(**body)
        except ValidationError as err:
            raise AssertionError(f"Ошибка валидации тела ответа.\n\n{err}")

    @staticmethod
    @allure.step("Проверка, что поле {field} равно {expected_value}")
    def assert_that_field_equal(
        data: dict[str, Any],
        field: str,
        expected_value: Any,
    ) -> None:
        actual_value = data[field]
        assert actual_value == expected_value, (
            f"Неверное значение поля {field}.\n"
            f"Ожидалось: {expected_value}.\nАктуальное: {actual_value}."
        )
