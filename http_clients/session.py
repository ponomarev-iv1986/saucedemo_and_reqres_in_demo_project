import json
from typing import Any

import allure
import curlify
import requests
from allure_commons.types import AttachmentType
from requests import Response, Session


class CustomSession(Session):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        super().__init__()

    def request(self, method: str, url: str, *args: Any, **kwargs: Any) -> Response:
        response = super().request(
            method=method, url=f"{self.base_url}{url}", *args, **kwargs
        )
        with allure.step(f"{method} {url}"):
            curl = curlify.to_curl(response.request)
            allure.attach(
                body=curl.encode("utf8"),
                name="CURL",
                attachment_type=AttachmentType.TEXT,
                extension="txt",
            )
            allure.attach(
                body=str(response.status_code),
                name="response status code",
                attachment_type=AttachmentType.TEXT,
                extension="txt",
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=2).encode("utf8"),
                    name="response body",
                    attachment_type=AttachmentType.JSON,
                    extension="json",
                )
            except requests.exceptions.JSONDecodeError:
                allure.attach(
                    body="no body or not JSON",
                    name="response body",
                    attachment_type=AttachmentType.TEXT,
                    extension="txt",
                )
        return response
