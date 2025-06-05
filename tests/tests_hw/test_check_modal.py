from pages.modal_dialogs import ModalDialogs
from conftest import browser
import time



def test_check_modal(browser):
    try:
        modal_page = ModalDialogs(browser)
        modal_page.visit()

        modal_page.small_modal.click()
        time.sleep(2)
        modal_page.close_small_modal.click()

        modal_page.large_modal.click()
        time.sleep(2)
        modal_page.close_large_modal.click()
    except:
        pass