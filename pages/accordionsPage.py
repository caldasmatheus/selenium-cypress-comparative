from pages.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class AccordionsPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def abrir_accordion(self, numero):
        self.find(By.XPATH, f"//button[text()='Accordion {numero}']").click()

    def clicar_botao(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def obter_texto_p(self, css_selector):
        return self.find(By.CSS_SELECTOR, css_selector).text

    def double_click_botao(self, data_testid):
        elemento = self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]")
        ActionChains(self.driver).double_click(elemento).perform()

    def right_click_botao(self, data_testid):
        elemento = self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]")
        ActionChains(self.driver).context_click(elemento).perform()

    def clicar_opcao_radio(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def clicar_checkbox(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def obter_texto_container(self):
        return self.find(By.CSS_SELECTOR, ".component-container > p").text

    def obter_texto_checkbox(self, index):
        return self.find(By.CSS_SELECTOR, f".checkbox-container:nth-child({index}) p").text