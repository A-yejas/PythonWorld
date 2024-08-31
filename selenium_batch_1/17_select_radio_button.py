from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

# Open a URL
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(5)
driver.execute_script("window.scrollTo(300, 400)")
time.sleep(3)


# Select radio button
driver.find_element_by_xpath('//*[text()="Male"]').click()

time.sleep(10)
driver.close()