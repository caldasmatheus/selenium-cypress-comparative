from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    APP_URL = "https://commitquality.com"

    def __init__(self, driver):
        self.driver = driver

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_element(self, element_tuple, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(element_tuple))
    
    def find(self, by, value):
        return self.driver.find_element(by, value)
    
    def navigate(self, url):
        self.driver.get(url)

    def navigate_to_app(self, path=''):
        full_url = f"{self.APP_URL}{path}"
        self.navigate(full_url)