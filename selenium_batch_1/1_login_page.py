from selenium import webdriver
import selenium
import time

# To Know selenium VERSION
print(' \n SELENIUM VERSION IS :: ', selenium.__version__)


# Open a Browser 
# driver = webdriver.Chrome()
# time.sleep(3)

## If Chrome driver in different path
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
#
## To Maximize window
driver.maximize_window()
time.sleep(3)

## Open a URL
driver.get('https://www.gmail.com')
time.sleep(3)

## To enter username in text box based on ID Locator
uname = driver.find_element_by_name('identifier')
uname.send_keys('xxxxh@gmail.com')
time.sleep(5)
Next = driver.find_element_by_xpath("//span[text() = 'Next']").click()
time.sleep(5)

## To enter password in text box based on name Locator
time.sleep(5)
password = driver.find_element_by_name('password')
password.send_keys('xxxxxx')
time.sleep(5)

## To click on login button
login_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[3]/button')
login_button.click()

## Close a browser
driver.close()

