from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)


    def get_url(self):
        return  self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return  True
        else:
            return False

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def get_title(self):
        return self.driver.title

    def refresh(self):
        self.driver.refresh()

