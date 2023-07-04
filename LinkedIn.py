from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://in.linkedin.com/")

InputElement = driver.find_element(By.ID, "session_key")
InputElement.send_keys("Abhinav.S.Raut@outlook.com")

InputPassword = driver.find_element(By.ID, "session_password")
InputPassword.send_keys("Abhinav@123")

driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/button").click()
