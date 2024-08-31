from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

d = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
d.get('https://www.facebook.com')
d.maximize_window()
time.sleep(5)

# Take screenshot
d.save_screenshot(r'C:\Users\Yejas\Desktop\Batch-9\PYTHON999.png')
d.close()