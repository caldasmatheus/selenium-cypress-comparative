from pages.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DragAndDropPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def mover_elemento(self, src_selector, dst_selector):
        src_element = self.find(By.CSS_SELECTOR, src_selector)
        dst_element = self.find(By.CSS_SELECTOR, dst_selector)
        ActionChains(self.driver).drag_and_drop(src_element, dst_element).perform()

    def obter_texto_elemento(self, selector):
        return self.find(By.CSS_SELECTOR, selector).text