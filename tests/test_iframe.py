import pytest
from selenium.webdriver.common.by import By
from pages.iframePage import IframePage

@pytest.fixture(scope="function")
def iframe_page(driver):
    page = IframePage(driver)
    page.abrir_pagina('/practice-iframe')
    yield page

def test_click_element_inside_iframe(iframe_page):
    assert iframe_page.obter_texto_cabecalho() == "IFrame"

    iframe_element = iframe_page.find(By.CSS_SELECTOR, "[data-testid=iframe]")
    iframe_page.driver.switch_to.frame(iframe_element)

    iframe_page.find(By.CSS_SELECTOR, "[data-testid=navbar-addproduct]").click()

    titulo_iframe = iframe_page.find(By.CSS_SELECTOR, "h1").text

    iframe_page.driver.switch_to.default_content()

    assert titulo_iframe == "Add Product"
    assert iframe_page.obter_texto_cabecalho() == "IFrame"