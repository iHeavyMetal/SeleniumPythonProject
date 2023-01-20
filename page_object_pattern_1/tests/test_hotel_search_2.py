import pytest

from page_object_pattern_1.pages.search_hotel import SearchHotelPage
from page_object_pattern_1.pages.search_results import SearchResultsPage
import allure
from page_object_pattern_1.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHotelSearch(BaseTest):
    @allure.title("Tis is title")
    @allure.description("Test description")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("23/01/2023", "30/01/2023")
        search_hotel_page.set_travellers("4", "4")
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert price_values[0] == "$22"
        assert price_values[1] == "$50"
        assert price_values[2] == "$80"
        assert price_values[3] == "$150"