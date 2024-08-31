from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

###  IF driver in current path ###
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)
#Zoom size
driver.execute_script("window.scrollTo(300, 500)")
time.sleep(5)
select_element = driver.find_element_by_id('RESULT_RadioButton-9')
time.sleep(5)
months = Select(select_element)
# time.sleep(5)
## To select a value based on visable text
# months.select_by_visible_text('Afternoon')
# time.sleep(5)

## To select a value based on value
# months.select_by_value('Radio-2')
# time.sleep(5)
time.sleep(5)
## To select a value based on index
months.select_by_index(1)
time.sleep(3)
# time.sleep(3)
driver.close()





