from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    """Base element class that represents a single element on a page"""

    def __init__(self, locator):
        self.locator = locator

    def wait_until(self, condition, driver):
        """Waits for the element to meet the specified condition"""
        return WebDriverWait(driver, 10).until(condition(self.locator))

    def wait_until_visible(self, driver):
        """Waits for the element to be visible"""
        return self.wait_until(EC.visibility_of_element_located, driver)

    def wait_until_not_visible(self, driver):
        """Waits for the element to be invisible"""
        return self.wait_until(EC.invisibility_of_element_located, driver)

    def wait_until_clickable(self, driver):
        """Waits for the element to be clickable"""
        return self.wait_until(EC.element_to_be_clickable, driver)

    def __get__(self, instance, owner):
        """Returns the element when accessed as an attribute of a PageObject"""
        driver = instance.driver
        return self.wait_until_visible(driver)

class InputElement(BaseElement):
    """Input element class that represents a text input field on a page"""

    def __init__(self, locator):
        super().__init__(locator)

    def clear(self, driver):
        """Clears the value of the input element"""
        element = self.wait_until_visible(driver)
        element.clear()

    def send_keys(self, driver, value):
        """Sets the value of the input element"""
        element = self.wait_until_visible(driver)
        element.send_keys(value)

    def get_text(self, driver):
        """GET TEXT"""
        element = self.wait_until_visible(driver)
        return element.text

class ActionElement(BaseElement):
    """Action element class that represents a clickable element on a page"""

    def __init__(self, locator):
        super().__init__(locator)

    def click(self, driver):
        """Clicks the element"""
        # self.wait_until_clickable(driver)()
        element = self.wait_until_clickable(driver)
        element.click()

