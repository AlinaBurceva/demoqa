from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

class WebElement:

    def __init__(self, driver, locator='',  locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
    #self.get_by_type()


    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click()

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return self.find_element().text

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print(f'Locator type {self.locator_type} not correct')
        return False

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:

        if len(self.find_elements()) == count:
            return  True
        return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)



