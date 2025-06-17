from pages.modal_dialogs import ModalDialogs
from conftest import browser
import requests
import pytest
import time



def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    try:
        response = requests.get('https://demoqa.com/modal-dialogs')
        response.raise_for_status()

    except requests.exceptions.RequestException:
        pytest.skip("Страница недоступна, пропускаем тест")

        assert modal_page.small_modal_btn.exist()
        assert modal_page.large_modal_btn.exist()
        modal_page.small_modal_btn.click()
        assert modal_page.small_modal.exist()
        time.sleep(2)
        assert modal_page.close_small_modal.exist()
        modal_page.close_small_modal.click()
        time.sleep(2)

        assert not modal_page.small_modal.exist()
        modal_page.large_modal_btn.click()
        time.sleep(2)
        assert modal_page.close_large_modal.exist()
        assert modal_page.small_modal.exist()
        modal_page.close_large_modal.click()
        time.sleep(2)
        assert not modal_page.small_modal.exist()
