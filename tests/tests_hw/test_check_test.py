from pages.demoqa import  DemoQa
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    actual_footer_text = demo_qa_page.footer_text.get_text()
    expected_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert actual_footer_text == expected_footer_text

def test_elements_center_text(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    actual_el_center_text = el_page.center_text.get_text()
    expected_el_center_text = 'Please select an item from left to start practice.'
    assert actual_el_center_text == expected_el_center_text

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()



