import pytest
from pages.dragAndDropPage import DragAndDropPage

@pytest.fixture(scope="function")
def drag_and_drop_page(driver):
    page = DragAndDropPage(driver)
    page.abrir_pagina('/practice-drag-and-drop')
    yield page

def test_drag_and_drop(drag_and_drop_page):
    drag_and_drop_page.mover_elemento("[data-testid=small-box]", "[data-testid=large-box]")

    texto = drag_and_drop_page.obter_texto_elemento("[data-testid=large-box]")
    assert texto == "Success!"