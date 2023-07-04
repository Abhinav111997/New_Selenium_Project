from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome("C://Users//90219//Downloads//chromedriver_win32 (1)//chromedriver.exe")
driver.get("https://seleniumbase.io/demo_page")

inputElement = driver.find_element(By.XPATH, '//*[@id="mySelect"]/option[2]')
inputElement.click()        # Manual way to do this.. which creates complexity when we multiple combinations

#----------------------------------------------------------------------------------------------------------------------------

inputElement = driver.find_element(By.ID, "mySelect")
dropdown = Select(inputElement)

time.sleep(3)
dropdown.select_by_index(3)

time.sleep(3)
dropdown.select_by_value("50%")

time.sleep(3)
dropdown.select_by_visible_text("Set to 75%")

all_options = dropdown.options
print(all_options)
