from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs


def test_page_dialogs(browser):
    modal_dia = ModalDialogs(browser)
    modal_dia.visit()
    assert modal_dia.submenu_items.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dia = ModalDialogs(browser)
    demo_qa = DemoQa(browser)

    modal_dia.visit()
    modal_dia.refresh()
    modal_dia.icon.click()
    demo_qa.back()
    browser.set_window_size(900, 400)
    demo_qa.forward()
    assert demo_qa.equal_url()
    assert demo_qa.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)