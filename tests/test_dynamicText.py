import pytest
from pages.dynamicTextPage import DynamicTextPage

@pytest.fixture(scope="function")
def dynamic_text_page(driver):
    page = DynamicTextPage(driver)
    page.abrir_pagina('/practice-dyanmic-text')
    yield page

def test_wait_button_change_text(dynamic_text_page):
    boton_selector = "[data-testid=dynamic-button1]"
    dynamic_text_page.clicar_botao(boton_selector)

    assert dynamic_text_page.obter_texto_botao(boton_selector) == "loading"

    dynamic_text_page.esperar_texto(boton_selector, "I am visible after 5 seconds", timeout=10)

    assert dynamic_text_page.obter_texto_botao(boton_selector) == "I am visible after 5 seconds"