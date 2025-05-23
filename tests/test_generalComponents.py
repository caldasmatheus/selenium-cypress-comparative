import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.generalComponentsPage import GeneralComponentsPage

@pytest.fixture(scope='function')
def general_components_page(driver):
    page = GeneralComponentsPage(driver)
    page.abrir_pagina('/practice-general-components')
    yield page

class TestGeneralComponents:

    def test_basic_click_button(self, general_components_page):
        general_components_page.clicar_botao('basic-click')
        assert general_components_page.obter_texto("[data-testid=basic-click]+p") == "Button clicked"

    def test_double_click_button(self, general_components_page):
        general_components_page.double_click("double-click")
        assert general_components_page.obter_texto("[data-testid=double-click]+p") == "Button double clicked"

    def test_right_click_button(self, general_components_page):
        general_components_page.right_click("right-click")
        assert general_components_page.obter_texto("[data-testid=right-click]+p") == "Button right mouse clicked"

    def test_click_radio_buttons(self, general_components_page):
        general_components_page.clicar_botao("option1")
        assert general_components_page.obter_texto(".radio-buttons-container p") == "option1 clicked"
        general_components_page.clicar_botao("option2")
        assert general_components_page.obter_texto(".radio-buttons-container p") == "option2 clicked"

    def test_select_option(self, general_components_page):
        general_components_page.selecionar_opcao("dropdown", "Option 3")
        dropdown = Select(general_components_page.driver.find_element(By.CSS_SELECTOR, "[data-testid=dropdown] > select"))
        assert dropdown.first_selected_option.text == "Option 3"

    def test_click_checkboxes(self, general_components_page):
        general_components_page.marcar_checkbox("checkbox1")
        assert general_components_page.obter_texto(".checkbox-container:nth-child(1) p") == "Checkbox 1 checked"
        general_components_page.marcar_checkbox("checkbox2")
        assert general_components_page.obter_texto(".checkbox-container:nth-child(2) p") == "Checkbox 2 checked"
        general_components_page.marcar_checkbox("checkbox3")
        assert general_components_page.obter_texto(".checkbox-container:nth-child(3) p") == "Checkbox 3 checked"

    def test_link_navigate_to_different_domain(self, general_components_page):
        general_components_page.abrir_link("link-same-tab")
        assert general_components_page.driver.current_url == "https://www.youtube.com/@commitquality"

    def test_link_opens_popup_on_different_domain(self, general_components_page):
        general_components_page.abrir_link("link-newtab")
        general_components_page.trocar_para_ultima_janela()
        assert general_components_page.driver.current_url == "https://www.youtube.com/@commitquality"

    def test_link_opens_popup_on_same_domain(self, general_components_page):
        general_components_page.abrir_link("link-newtab-practice")
        general_components_page.trocar_para_ultima_janela()
        assert general_components_page.driver.current_url.endswith("/practice")