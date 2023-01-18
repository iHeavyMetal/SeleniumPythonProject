from selenium.webdriver.common.by import By


class GoogleResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_result_css = '.LC20lb'

    def open_first_result(self):
        list_link = self.driver.find_elements(By.CSS_SELECTOR, self.search_result_css)
        print(list_link)
        list_link[0].click()
