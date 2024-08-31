from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

d = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32 (1)/chromedriver.exe")
# d = chrome_executable_path = ChromeDriverManager().install()
d.maximize_window()
d.get("http://testautomationpractice.blogspot.com/")
sleep(5)

d.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

alert = d.switch_to.alert

#  To get alert message
print(' \n\n ' , alert.text)
sleep(5)

## To accept alert
# alert.accept()
alert.dismiss()
# alert.accept()  – used to accept the Alert
# alert.dismiss() – used to cancel the Alert
# alert.send_keys(' Yejas ') – used to enter a value in the Alert text box.

sleep(5)
d.close()

