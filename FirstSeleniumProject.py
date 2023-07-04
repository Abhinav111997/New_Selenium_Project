print('Hello Abhinav....')

from selenium import webdriver

driver = webdriver.Chrome("C://Users//90219//Downloads//chromedriver_win32//chromedriver.exe")
driver.get("http://www.youtube.com/")

print("Page title :", driver.title)                        # YouTube
print(" Page Current URL :", driver.current_url)           # https://www.youtube.com/

driver.get("http://www.flipkart.com/")
print("Page title :", driver.title)                        #Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!
print(" Page Current URL :", driver.current_url)           # https://www.flipkart.com/

driver.close()                                             # closed current window
driver.quit()                                              # closed all windows
