from selenium import webdriver
import time

# Chrome path
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")

# maximize the window size
driver.maximize_window()

# passing URL
driver.get("https://www.python.org")

## click on specified element
time.sleep(10)

driver.find_element_by_id('documentation').click()
time.sleep(10)
# Navigate to Back
driver.back()
time.sleep(10)
# Navigate to forward
driver.forward()

time.sleep(10)
# Closing the browser

driver.close()

