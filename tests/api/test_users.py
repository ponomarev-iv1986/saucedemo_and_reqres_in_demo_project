import allure
import pytest
from allure_commons.types import Severity

from models.reqres_in_models import ListUsers, SingleUser


@allure.title("Проверка получения списка пользователей")
@allure.severity(Severity.CRITICAL)
@allure.tag("API", "REGRESS")
@allure.suite("Пользователи")
@allure.parent_suite("Тесты API")
@pytest.mark.parametrize("page, per_page", [(1, 2), (1, 6), (2, 4)])
def test_list_users(reqres_http_client, page, per_page):
    response = reqres_http_client.list_users(page, per_page)
    reqres_http_client.assert_that_status_code_equal(response, 200)

    body = response.json()
    reqres_http_client.validate_model(body, ListUsers)
    reqres_http_client.assert_that_field_equal(body, "page", page)
    reqres_http_client.assert_that_field_equal(body, "per_page", per_page)


@allure.title("Проверка получения пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("API", "REGRESS")
@allure.suite("Пользователи")
@allure.parent_suite("Тесты API")
@pytest.mark.parametrize(
    "user_id, first_name, last_name",
    [
        pytest.param(1, "George", "Bluth", id="George Bluth"),
        pytest.param(2, "Janet", "Weaver", id="Janet Weaver"),
        pytest.param(3, "Emma", "Wong", id="Emma Wong"),
        pytest.param(4, "Eve", "Holt", id="Eve Holt"),
        pytest.param(5, "Charles", "Morris", id="Charles Morris"),
        pytest.param(6, "Tracey", "Ramos", id="Tracey Ramos"),
        pytest.param(7, "Michael", "Lawson", id="Michael Lawson"),
        pytest.param(8, "Lindsay", "Ferguson", id="Lindsay Ferguson"),
        pytest.param(9, "Tobias", "Funke", id="Tobias Funke"),
        pytest.param(10, "Byron", "Fields", id="Byron Fields"),
        pytest.param(11, "George", "Edwards", id="George Edwards"),
        pytest.param(12, "Rachel", "Howell", id="Rachel Howell"),
    ],
)
def test_retrieve_user(reqres_http_client, user_id, first_name, last_name):
    response = reqres_http_client.retrieve_user(user_id)
    reqres_http_client.assert_that_status_code_equal(response, 200)

    body = response.json()
    data = body["data"]
    reqres_http_client.validate_model(body, SingleUser)
    reqres_http_client.assert_that_field_equal(data, "first_name", first_name)
    reqres_http_client.assert_that_field_equal(data, "last_name", last_name)


@allure.title("Проверка получения несуществующего пользователя")
@allure.severity(Severity.NORMAL)
@allure.tag("API", "REGRESS")
@allure.suite("Пользователи")
@allure.parent_suite("Тесты API")
def test_user_not_found(reqres_http_client):
    response = reqres_http_client.retrieve_user(15)
    reqres_http_client.assert_that_status_code_equal(response, 404)
