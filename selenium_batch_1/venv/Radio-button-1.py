import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch Firefox browser
d = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
# time.sleep(3)
''' Maximize the window size '''
d.maximize_window()

d.get("http://www.zkoss.org/zkdemo/input/radio_button")
time.sleep(2)

''' Clicking the Radio buttons'''

for i in d.find_elements_by_xpath("//*[@type ='radio']"):
    i.click()
    time.sleep(1)

time.sleep(3)

# closing the browser
d.close()

