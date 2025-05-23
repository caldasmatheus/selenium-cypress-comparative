from pages.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicTextPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def clicar_botao(self, selector):
        self.find(By.CSS_SELECTOR, selector).click()

    def obter_texto_botao(self, selector):
        return self.find(By.CSS_SELECTOR, selector).text

    def esperar_texto(self, selector, texto_esperado, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, selector), texto_esperado)
        )