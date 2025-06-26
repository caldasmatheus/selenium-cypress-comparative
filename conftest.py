import pytest
from pages.accordionsPage import AccordionsPage
from pages.contactUsFormPage import ContactUsFormPage
from pages.dragAndDropPage import DragAndDropPage
from pages.dynamicTextPage import DynamicTextPage
from pages.fileUploadPage import FileUploadPage
from pages.generalComponentsPage import GeneralComponentsPage
from pages.iframePage import IframePage
from pages.practicePage import PracticePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="session")
def driver(request):
    chrome_options = Options()
    if os.getenv('HEADLESS') or request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="run tests in headless mode")

@pytest.fixture(scope="function")
def setup_teardown(driver):
    accordions_page = AccordionsPage(driver)
    contactUsForm_page = ContactUsFormPage(driver)
    dragAndDrop_page = DragAndDropPage(driver)
    dynamicText_page = DynamicTextPage(driver)
    fileUpload_page = FileUploadPage(driver)
    generalComponents_page = GeneralComponentsPage(driver)
    iframe_page = IframePage(driver)
    practice_page = PracticePage(driver)

    accordions_page.abrir_pagina('/practice-accordions')
    contactUsForm_page.abrir_pagina('/practice-contact-form')
    dragAndDrop_page.abrir_pagina('/practice-drag-and-drop')
    dynamicText_page.abrir_pagina('/practice-dyanmic-text')
    fileUpload_page.abrir_pagina('/practice-file-upload')
    generalComponents_page.abrir_pagina('/practice-general-components')
    iframe_page.abrir_pagina('/practice-iframe')
    practice_page.abrir_pagina('/practice-api')

    yield accordions_page, contactUsForm_page, dragAndDrop_page, dynamicText_page, fileUpload_page, generalComponents_page, iframe_page, practice_page