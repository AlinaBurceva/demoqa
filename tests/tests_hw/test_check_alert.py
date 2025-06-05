from conftest import browser
from pages.alerts import Alerts
import time

def test_timer(browser):
    alerts = Alerts(browser)

    alerts.visit()
    assert not alerts.alert()

    alerts.timer_alert.click_force()
    time.sleep(10)
    assert alerts.alert()
    assert alerts.alert().text == 'This alert appeared after 5 seconds'