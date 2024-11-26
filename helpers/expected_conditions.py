from typing import Callable

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import \
    WebDriverOrWebElement


def count_of_elements_equal(
    locator: tuple[str, str],
    count: int,
) -> Callable[[WebDriverOrWebElement], bool]:

    def _predicate(driver: WebDriverOrWebElement):
        try:
            elements = driver.find_elements(*locator)
            return len(elements) == count
        except StaleElementReferenceException:
            return False

    return _predicate
