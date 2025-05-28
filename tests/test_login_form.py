import time
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('testerov')
    form_page.last_name.send_keys('testerovs')
    form_page.user_email.send_keys('test@test.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('111222333444')
    form_page.hobbies_radio_1.click_force()
    form_page.current_address.send_keys('what a fuck')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(3)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()