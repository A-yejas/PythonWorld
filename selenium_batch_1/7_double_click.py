from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")

# Move cursor on specified element and click
obj = driver.find_element_by_xpath('//*[@id="authentication"]/button')
time.sleep(3)
actions = ActionChains(driver)
actions.move_to_element(obj)
time.sleep(3)
actions.double_click()
time.sleep(2)
actions.perform()

time.sleep(5)
driver.quit()
