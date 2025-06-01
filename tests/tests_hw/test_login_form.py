import time
from pages.form_page import FormPage


def test_login_form_hw(browser):
    reg_form = FormPage(browser)
    reg_form.visit()
    assert not reg_form.modal_dialog.exist()
    time.sleep(3)
    reg_form.first_name.send_keys('tester')
    reg_form.last_name.send_keys('testerovich')
    reg_form.user_email.send_keys('test@test.tt')
    reg_form.gender_radio_1.click_force()
    reg_form.user_number.send_keys('111222333444')
    reg_form.hobbies_radio_1.click_force()
    reg_form.current_address.send_keys('what a fuck')
    time.sleep(2)
    reg_form.btn_state.scroll_to_element()
    reg_form.btn_state.click()
    reg_form.btn_NCR.click()
    time.sleep(2)

    reg_form.btn_submit.click_force()
    time.sleep(3)

    assert reg_form.modal_dialog.exist()
    reg_form.btn_close_modal.click_force()