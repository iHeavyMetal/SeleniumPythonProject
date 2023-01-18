class GoogleResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_result_xpath = "//he[@class='LC201b']"

    def open_first_result(self):
        self.driver.find_elements_by_xpath(self.search_result_xpath)[0].click()