from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://seleniumbase.io/demo_page")

inputTextField = driver.find_element(By.ID, "myTextInput")
inputTextField.send_keys("Hello")

inputTextArea = driver.find_element(By.ID, "myTextarea")
inputTextArea.send_keys("Nature")

inputTextHolderField = driver.find_element(By.ID, "myTextInput2")
inputTextHolderField.send_keys("Pravah")

inputElement = driver.find_element(By.ID, "dropOption1")
print("Is element displayed : ", inputElement.is_displayed())

#------------------------------------------------------------------------------------------------------------------

inputElement = driver.find_element(By.ID, "myTextInput")
print("Is element displayed : ", inputElement.is_displayed())

inputElement = driver.find_element(By.ID, "radioButton1")
print("Is element displayed : ", inputElement.is_selected())

inputElement = driver.find_element(By.ID, "radioButton2")
print("Is element displayed : ", inputElement.is_selected())
