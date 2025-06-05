from pages.webtables_page import WebTables
from conftest import browser
import time

def test_sort(browser):
    tables_page = WebTables(browser)
    table_class_1 = 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    table_class_2 = 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

    tables_page.visit()

    #FirstName 2 clicks
    for i in range(2):
        tables_page.first_name.click()
    assert tables_page.first_name.get_dom_attribute('class') == table_class_1 or table_class_2
    time.sleep(2)

    #LastName 1 click
    tables_page.last_name.click()
    time.sleep(1)
    assert tables_page.last_name.get_dom_attribute('class') == table_class_1 or table_class_2

    #Age 2 clicks
    for i in range(2):
        tables_page.age.click()
        assert tables_page.age.get_dom_attribute('class') == table_class_1 or table_class_2

    #Email 1 click
    tables_page.email.click()
    assert tables_page.email.get_dom_attribute('class') == table_class_1 or table_class_2

    #Salary 2 clicks
    for i in range(2):
        tables_page.salary.click()
        assert tables_page.salary.get_dom_attribute('class') == table_class_1 or table_class_2

    #Department 1 click
    tables_page.department.click()
    assert tables_page.department.get_dom_attribute('class') == table_class_1 or table_class_2