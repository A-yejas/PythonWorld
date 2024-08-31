from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")
time.sleep(5)

driver.execute_script("document.body.style.zoom='300%'")
time.sleep(7)
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(5)
driver.close()