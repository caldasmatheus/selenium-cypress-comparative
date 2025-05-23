import pytest
from selenium.webdriver.common.by import By
from pages.contactUsFormPage import ContactUsFormPage

@pytest.fixture(scope='function')
def contact_us_form_page(driver):
    page = ContactUsFormPage(driver)
    page.abrir_pagina('/practice-contact-form')
    yield page

def test_successful_submit_form(contact_us_form_page):
    contact_us_form_page.preencher_nome("User Test")
    contact_us_form_page.preencher_email("user@test.com")
    contact_us_form_page.selecionar_query_type("Technical")
    contact_us_form_page.preencher_dob("01/01/2000")
    contact_us_form_page.clicar_checkbox()
    contact_us_form_page.clicar_submit()

    mensagem = contact_us_form_page.obter_mensagem_sucesso()
    assert mensagem == "Thanks for contacting us, we will never respond!"