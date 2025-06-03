from pages.webtables_page import WebTables
from conftest import browser
import time

def test_webtables(browser):
    webtable = WebTables(browser)

    webtable.visit()
    assert not webtable.no_data.exists()

    while webtable.btn_delete_row.exists():
        webtable.btn_delete_row.click()

    time.sleep(2)
    assert webtable.no_data.exists()