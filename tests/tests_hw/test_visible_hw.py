import time
from pages.accordion import Accordion

def test_visible_accordian(browser):
    acc_page = Accordion(browser)
    acc_page.visit()
    acc_page.section1.click()
    time.sleep(3)
    assert not acc_page.section1_p.visible()

def test_visible_accordian_default(browser):
    acc_page = Accordion(browser)
    acc_page.visit()
    assert not acc_page.section2_p_1.visible()
    assert not acc_page.section2_p_2.visible()
    assert not acc_page.section3_p.visible()