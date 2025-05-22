from selenium.webdriver.common.by import By

def test_check_icon(browser):
    #browser
    # driver = webdriver.Chrome()
    browser.get("http://demoqa.com/")
    icon = browser.find_element(By.CSS_SELECTOR, 'header > a > img') #app > header > a'
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')








