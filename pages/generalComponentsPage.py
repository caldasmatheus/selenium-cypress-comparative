from pages.basePage import Base
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GeneralComponentsPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def clicar_botao(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()
    
    def obter_texto(self, css_selector):
        return self.find(By.CSS_SELECTOR, css_selector).text

    def double_click(self, data_testid):
        element = self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]")
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, data_testid):
        element = self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]")
        ActionChains(self.driver).context_click(element).perform()

    def selecionar_opcao(self, data_testid, visible_text):
        dropdown = Select(self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}] > select"))
        dropdown.select_by_visible_text(visible_text)

    def marcar_checkbox(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def abrir_link(self, data_testid):
        self.find(By.CSS_SELECTOR, f"[data-testid={data_testid}]").click()

    def trocar_para_ultima_janela(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])