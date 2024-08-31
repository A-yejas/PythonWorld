import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Launch Firefox browser
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
# time.sleep(3)
driver.get("http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html")
for i in range(20):
    try:
        time.sleep(10)
        driver.find_element_by_xpath("//*[contains(text(), 'cb7: normal checkbox.')]").click()
        time.sleep(10)
        break
    except NoSuchElementException as e:
        print("First_batch")
        time.sleep(1)
else:
    print('Test Failed')
time.sleep(5)
driver.close()

time.sleep(6)
#18601207777--icici-personal-loan

