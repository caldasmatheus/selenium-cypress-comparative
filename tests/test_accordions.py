import pytest
from pages.accordionsPage import AccordionsPage

@pytest.fixture(scope="function")
def accordions_page(driver):
    page = AccordionsPage(driver)
    page.abrir_pagina('/practice-accordions')
    yield page

class TestAccordions:
    def test_basic_click_button_inside_accordion(self, accordions_page):
        accordions_page.abrir_accordion(1)
        accordions_page.clicar_botao('basic-click')
        assert accordions_page.obter_texto_p("[data-testid=basic-click]+p") == "Button clicked"

    def test_double_click_button_inside_accordion(self, accordions_page):
        accordions_page.abrir_accordion(1)
        accordions_page.double_click_botao('double-click')
        assert accordions_page.obter_texto_p("[data-testid=double-click]+p") == "Button double clicked"

    def test_right_click_button_inside_accordion(self, accordions_page):
        accordions_page.abrir_accordion(1)
        accordions_page.right_click_botao('right-click')
        assert accordions_page.obter_texto_p("[data-testid=right-click]+p") == "Button right mouse clicked"

    def test_click_radio_buttons_inside_accordion(self, accordions_page):
        accordions_page.abrir_accordion(2)
        accordions_page.clicar_opcao_radio('option1')
        assert accordions_page.obter_texto_container() == "option1 clicked"
        accordions_page.clicar_opcao_radio('option2')
        assert accordions_page.obter_texto_container() == "option2 clicked"

    def test_click_checkboxes_inside_accordion(self, accordions_page):
        accordions_page.abrir_accordion(3)
        accordions_page.clicar_checkbox('checkbox1')
        assert accordions_page.obter_texto_checkbox(1) == "Checkbox 1 checked"
        accordions_page.clicar_checkbox('checkbox2')
        assert accordions_page.obter_texto_checkbox(2) == "Checkbox 2 checked"
        accordions_page.clicar_checkbox('checkbox3')
        assert accordions_page.obter_texto_checkbox(3) == "Checkbox 3 checked"