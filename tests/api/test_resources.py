import allure
import pytest
from allure_commons.types import Severity

from models.reqres_in_models import ListResources, SingleResource


@allure.title("Проверка получения списка ресурсов")
@allure.severity(Severity.CRITICAL)
@allure.tag("API", "REGRESS")
@allure.suite("Ресурсы")
@allure.parent_suite("Тесты API")
@pytest.mark.parametrize("page, per_page", [(1, 2), (1, 6), (2, 4)])
def test_list_resources(reqres_http_client, page, per_page):
    response = reqres_http_client.list_resources(page, per_page)
    reqres_http_client.assert_that_status_code_equal(response, 200)

    body = response.json()
    reqres_http_client.validate_model(body, ListResources)
    reqres_http_client.assert_that_field_equal(body, "page", page)
    reqres_http_client.assert_that_field_equal(body, "per_page", per_page)


@allure.title("Проверка получения ресурса")
@allure.severity(Severity.CRITICAL)
@allure.tag("API", "REGRESS")
@allure.suite("Ресурсы")
@allure.parent_suite("Тесты API")
@pytest.mark.parametrize(
    "resource_id, name, year",
    [
        pytest.param(1, "cerulean", 2000, id="cerulean"),
        pytest.param(2, "fuchsia rose", 2001, id="fuchsia rose"),
        pytest.param(3, "true red", 2002, id="true red"),
        pytest.param(4, "aqua sky", 2003, id="aqua sky"),
        pytest.param(5, "tigerlily", 2004, id="tigerlily"),
        pytest.param(6, "blue turquoise", 2005, id="blue turquoise"),
        pytest.param(7, "sand dollar", 2006, id="sand dollar"),
        pytest.param(8, "chili pepper", 2007, id="chili pepper"),
        pytest.param(9, "blue iris", 2008, id="blue iris"),
        pytest.param(10, "mimosa", 2009, id="mimosa"),
        pytest.param(11, "turquoise", 2010, id="turquoise"),
        pytest.param(12, "honeysuckle", 2011, id="honeysuckle"),
    ],
)
def test_retrieve_resource(reqres_http_client, resource_id, name, year):
    response = reqres_http_client.retrieve_resource(resource_id)
    reqres_http_client.assert_that_status_code_equal(response, 200)

    body = response.json()
    data = body["data"]
    reqres_http_client.validate_model(body, SingleResource)
    reqres_http_client.assert_that_field_equal(data, "name", name)
    reqres_http_client.assert_that_field_equal(data, "year", year)


@allure.title("Проверка получения несуществующего ресурса")
@allure.severity(Severity.NORMAL)
@allure.tag("API", "REGRESS")
@allure.suite("Ресурсы")
@allure.parent_suite("Тесты API")
def test_resource_not_found(reqres_http_client):
    response = reqres_http_client.retrieve_resource(15)
    reqres_http_client.assert_that_status_code_equal(response, 404)
