from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

d = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32 (1)/chromedriver.exe")
# d = chrome_executable_path = ChromeDriverManager().install()
d.maximize_window()
d.get("https://tdp--qa--recruit.edgenetworks.ai/auth/Login")
sleep(5)
email = d.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div/div/div/div/form/div[1]/div/div/div/input")
sleep(5)
email.sendKeys('yejas')