from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://www.amazon.com")

inputElement = driver.find_element(By.ID, "searchDropdownBox")  # searchDropdownBox
inputElement.send_keys("Computers")

inputName = driver.find_element(By.NAME, "field-keywords")    # field-keywords
inputName.send_keys("Dell laptop")

print("Input ID: ",   inputElement.get_attribute("ID"))
print("Input Name: ", inputName.get_attribute("NAME"))

driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/span/div/h1/div/div[2]"
                              "/div/div/form/span/span/span/span").click()

InputSortNewestArrivals = driver.find_element(By.ID, "s-result-sort-select_4")
InputSortNewestArrivals.send_keys("Newest Arrivals")
driver.find_element(By.XPATH, "/html/body/div[4]/div/div/ul/li[5]").click()


