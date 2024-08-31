from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Users/Yejas/Downloads/chromedriver_win32/chromedriver.exe")
#
## To Maximize window
driver.maximize_window()
time.sleep(3)

## Open a URL
driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin')
time.sleep(3)

## To enter username in text box based on ID Locator
uname = driver.find_element_by_xpath("//*[@name='email']")
uname.send_keys('h@gmail.com')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='continue']").click()
time.sleep(5)



