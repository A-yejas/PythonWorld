from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(5)
driver.execute_script("window.scrollTo(300, 500)")

# Select Check box
obj = driver.find_element_by_xpath('//*[text()="Tuesday"]')
obj.click()
time.sleep(5)

driver.close()
