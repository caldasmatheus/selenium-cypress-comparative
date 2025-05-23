from pages.basePage import Base
from selenium.webdriver.common.by import By

class PracticePage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def abrir_pagina(self, url):
        self.navigate_to_app(url)
        
    def clicar_accordion(self, numero):
        self.find(By.XPATH, f"//button[text()='Accordion {numero}']").click()

    def clicar_botao(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def pegar_texto(self, css_selector):
        return self.find(By.CSS_SELECTOR, css_selector).text