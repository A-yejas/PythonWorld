'''
There are basically two types of wait statements: Implicit Wait and Explicit Wait.

Implicit wait instructs the WebDriver to wait for some time by polling the DOM.
Once you have declared implicit wait, it will be available for the entire life of the WebDriver instance.
By default,the value will be 0. If you set a longer default, then the behavior will poll the DOM on a
periodic basis depending on the browser/ driver implementation.

Explicit wait instructs the execution to wait for some time until some condition is achieved.
Some of those conditions to be attained are:
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://selenium-python.readthedocs.io")
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[5]/aaa').click()

driver.close()

