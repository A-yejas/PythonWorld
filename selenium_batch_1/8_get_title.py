from selenium import webdriver
import time

# Launch chrome browser
d = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
#maximize the window size
d.maximize_window()
#Pass URL
d.get('https://www.geeksforgeeks.org')

# To Get Window Title
w_title = d.title

print('\n Window title is : ', w_title)
time.sleep(3)
#Verified
# assert w_title == 'Welcome to Python.org' , ' Title is not matched '

#time
time.sleep(3)
#Closing the browser
d.close()

