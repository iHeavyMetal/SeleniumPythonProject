from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_object_pattern.pages.google_home_page import GoogleHomePage
from page_object_pattern.pages.google_result_page import GoogleResultPage

import pytest
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))



class TestGoogleSearch:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        self.driver.quit()

    def test_google_search(self,setup):
        self.driver.get("http://www.google.com")
        home_page = GoogleHomePage(self.driver)
        home_page.search_in_google("Selenium")
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()