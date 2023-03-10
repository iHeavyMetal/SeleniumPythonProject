import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()                                                 #Fix for automatically close Chrome
options.add_experimental_option("detach", True)                                     #Fix for automatically close Chrome
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))    #Fix for automatically close Chrome
driver.implicitly_wait(1)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

#driver.find_element(By.ID, "s2id_autogen8").click()
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element(By.XPATH, "//span[text()='Dubai']").click()

#1st method for setting the date on the calendar
#driver.find_element(By.NAME, "checkin").send_keys("23/01/2023")
#driver.find_element(By.NAME, "checkout").send_keys("30/01/2023")

#2nd method for setting the date on the calendar
driver.find_element(By.NAME, "checkin").click()
driver.find_element(By.XPATH, "//td[@class='day ' and text()='23']").click()
elements = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='30']")
for element in elements:
    if(element.is_displayed()):
        element.click()
        break

driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys("4")
driver.find_element(By.ID, "childInput").clear()
driver.find_element(By.ID, "childInput").send_keys("4")
driver.find_element(By.XPATH, "//button[text()=' Search']").click()

hotel_list = driver.find_elements(By.XPATH, "//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotel_list]
for name in hotel_names:
    print("Hotel name: " + name)

prices = driver.find_elements(By.XPATH, "//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Hotel price: " + price)

assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_values[0] == "$22"
assert price_values[1] == "$50"
assert price_values[2] == "$80"
assert price_values[3] == "$150"


#time.sleep(2)
driver.quit()