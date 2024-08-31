from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.python.org")
time.sleep(4)
## Get text based on xpath

text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

print('\n Text is :', text)


time.sleep(4)
driver.close()





