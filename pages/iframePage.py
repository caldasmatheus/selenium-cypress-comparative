from pages.basePage import Base
from selenium.webdriver.common.by import By

class IframePage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)
        
    def obter_texto_cabecalho(self):
        return self.find(By.CSS_SELECTOR, "h2").text
    
    def clicar_em_elemento_no_iframe(self, data_testid):
        iframe = self.find(By.CSS_SELECTOR, "[data-testid=iframe]")
        self.driver.switch_to.frame(iframe)
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()
        self.driver.switch_to.default_content()

    def obter_titulo_no_iframe(self):
        # Supondo que o título dentro do iframe seja um h1
        return self.find(By.CSS_SELECTOR, "h1").text

    def obter_titulo_fora_do_iframe(self):
        return self.find(By.CSS_SELECTOR, "h2").text