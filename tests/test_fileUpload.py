import pytest
import os
from pathlib import Path
from pages.fileUploadPage import FileUploadPage

@pytest.fixture(scope="function")
def file_upload_page(driver):
    page = FileUploadPage(driver)
    page.abrir_pagina('/practice-file-upload')
    yield page

def test_file_upload(file_upload_page):
    arquivo_path = str(Path("").absolute() / "pom.xml")
    
    file_upload_page.fazer_upload(arquivo_path)

    file_upload_page.clicar_enviar()

    mensagem = file_upload_page.obter_alerta_texto()
    assert mensagem == "File successfully uploaded!"