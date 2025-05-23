from pages.basePage import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactUsFormPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def preencher_nome(self, nome):
        self.find(By.CSS_SELECTOR, "[data-testid=name]").send_keys(nome)

    def preencher_email(self, email):
        self.find(By.CSS_SELECTOR, "[data-testid=email]").send_keys(email)

    def selecionar_query_type(self, visible_text):
        select_element = self.find(By.CSS_SELECTOR, "[data-testid=query-type]")
        Select(select_element).select_by_visible_text(visible_text)

    def preencher_dob(self, data):
        self.find(By.CSS_SELECTOR, "[data-testid=dob]").send_keys(data)

    def clicar_checkbox(self):
        self.find(By.CSS_SELECTOR, "[data-testid=practice-checkbox]").click()

    def clicar_submit(self):
        self.find(By.CSS_SELECTOR, "[data-testid=submit-button]").click()

    def obter_mensagem_sucesso(self):
        return self.find(By.CSS_SELECTOR, ".success-message").text