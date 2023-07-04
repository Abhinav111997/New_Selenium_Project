from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("http://www.facebook.com/")

InputEmail = driver.find_element(By.ID, "email")
InputEmail.send_keys("9657882037")

InputPassword = driver.find_element(By.ID, "pass")
InputPassword.send_keys("Abhinav@123")

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div"
                              "/div/div/div[2]/div/div[1]/form/div[2]/button").click()