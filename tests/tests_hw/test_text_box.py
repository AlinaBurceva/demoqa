import time
from pages.text_box import TextBox

def test_text_box(browser):
    text_form = TextBox(browser)
    text_form.visit()
    text_form.full_name.send_keys('Alina')
    text_form.curr_address.send_keys('Spb')
    time.sleep(5)
    text_form.btn_submit.click_force()
    time.sleep(5)

    expected_result_name = 'Name:Alina'
    expected_curr_address = 'Current Address :Spb'

    actual_result_name = text_form.name_result.get_text()
    actual_result_curr_add = text_form.curr_address_result.get_text()

    assert actual_result_name == expected_result_name and actual_result_curr_add == expected_curr_address