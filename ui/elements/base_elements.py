from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement:
    """Base element class that represents a single element on a page"""

    def __init__(self, locator):
        self.locator = locator

    def wait_until(self, condition, driver) -> WebElement:
        """
        Waits for the element to meet the specified condition
        :param condition: condition for wait
        :param driver: driver instance
        :return: element that meets condition
        """
        return WebDriverWait(driver, 10).until(condition(self.locator))

    def wait_until_visible(self, driver) -> WebElement:
        """
        Waits for the element to be visible
        :param driver: driver instance
        :return: visible element
        """
        return self.wait_until(ec.visibility_of_element_located, driver)

    def wait_until_not_visible(self, driver) -> WebElement:
        """
        Waits for the element to be invisible
        :param driver: driver instance
        :return: invisible element
        """
        return self.wait_until(ec.invisibility_of_element_located, driver)

    def wait_until_clickable(self, driver) -> WebElement:
        """
        Waits for the element to be clickable
        :param driver: driver instance
        :return: clickable element
        """
        return self.wait_until(ec.element_to_be_clickable, driver)

    def __get__(self, instance, owner) -> WebElement:
        """
        Returns the element when accessed as an attribute of a PageObject
        :param instance: class instance
        :param owner: type
        :return: WebElement
        """
        driver = instance.driver
        return self.wait_until_visible(driver)


class InputElement(BaseElement):
    """Input element class that represents a text input field on a page"""

    def __init__(self, locator):
        super().__init__(locator)

    def clear(self, driver) -> None:
        """
        Clears the value of the input element
        :param driver: driver instance
        :return: None
        """
        element = self.wait_until_visible(driver)
        element.clear()

    def send_keys(self, driver, value) -> None:
        """
        Sets the value of the input element
        :param driver: driver instance
        :param value: value to be set
        :return: None
        """
        element = self.wait_until_visible(driver)
        element.send_keys(value)

    def get_text(self, driver) -> str:
        """
        Get the text
        :param driver: driver instance
        :return: text
        """
        element = self.wait_until_visible(driver)
        return element.text


class ActionElement(BaseElement):
    """Action element class that represents a clickable element on a page"""

    def __init__(self, locator):
        super().__init__(locator)

    def click(self, driver) -> None:
        """
        Clicks the element
        :param driver: driver instance
        :return: None
        """
        element = self.wait_until_clickable(driver)
        element.click()
