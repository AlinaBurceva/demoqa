from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.curr_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.name_result = WebElement(driver, '#name')
        self.curr_address_result = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[2]', 'xpath')

