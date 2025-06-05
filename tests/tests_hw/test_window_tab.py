from pages.links_page import LinksPage
from conftest import browser
import time


def test_linkspage(browser):
    links_page = LinksPage(browser)

    links_page.visit()
    assert len(browser.window_handles) == 1

    assert links_page.home_link.get_text() == 'Home'
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    links_page.home_link.click()
    time.sleep(1)
    assert len(browser.window_handles) == 2