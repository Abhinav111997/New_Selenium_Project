from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("https://mathup.com/")

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]").click()

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[1]/div/div/div[5]/div/div[1]/div[2]/div[1]/div[2]").click()



