from pages.basePage import Base
from selenium.webdriver.common.by import By

class FileUploadPage(Base):
    
    def __init__(self, driver):
        super().__init__(driver)

    def abrir_pagina(self, url):
        self.navigate_to_app(url)

    def fazer_upload(self, file_path):
        self.find(By.CSS_SELECTOR, "[data-testid=file-input]").send_keys(file_path)

    def clicar_enviar(self):
        self.find(By.CSS_SELECTOR, ".file-upload button[type=submit]").click()

    def obter_alerta_texto(self):
        alert = self.driver.switch_to.alert
        texto = alert.text
        alert.accept()
        return texto