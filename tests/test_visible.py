import time
from pages.elements_page import ElementsPage

# def test_visible_btn_sidebar(browser):
#     elements = ElementsPage(browser)
#     elements.visit()
#     assert elements.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    elements = ElementsPage(browser)
    elements.visit()

    assert elements.btn_sidebar_first_checkbox.visible()
    elements.btn_sidebar_first.click()
    time.sleep(2)

    assert not elements.btn_sidebar_first_checkbox.visible()