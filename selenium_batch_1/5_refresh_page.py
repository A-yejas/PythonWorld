from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time

''' Refresh the Page'''

# driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32(1)/chromedriver.exe")
driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
# driver = ChromeDriverManager().install()
driver.maximize_window()
driver.get("http://www.facebook.com")

time.sleep(10)
driver.refresh()
time.sleep(10)
driver.refresh()
time.sleep(10)
driver.close()



