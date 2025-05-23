import pytest
from pages.practicePage import PracticePage

@pytest.fixture(scope='function')
def practice_page(driver):
    page = PracticePage(driver)
    page.abrir_pagina('/practice-api')
    yield page

def test_capture_api_response(practice_page):
    pass