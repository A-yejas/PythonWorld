## Please complete below steps one by one
"""
1. Install Selenium

2. Find selenium Version

3. Creare seperate folder for you selenium scripts

4. download required chrome driver and place in your selenium scripts folder
    # Link for download chrome driver : https://chromedriver.storage.googleapis.com/index.html

5. create a login_page.py file inside selenium diractory

6. write code for below actions inside login_page.py file 
    
    1. import webdriver from selenium
    2. create a driver for Chrome brower
    3. Maximize browser window
    4. Enter login page URL('https://accounts.lambdatest.com/login')
    5. Find element for uname text box
    6. Enter uname
    7. Find element for password text box
    8. Enter password
    9. Find element for login button text box
   10. Click on login button 
   11. Colse browser
"""
'''
# Locating by ID
ID’s are supposed to be unique for each element.

Target Format: id=id of the element
#XPATH: - XPath in Selenium is an XML path used for navigation through the HTML structure of the page. 
It is a syntax or language for finding any element on a web page using XML path expression.
Xpath :- //tagename[@attribute = 'value']
###
// : Select current node.
Tagname: Tagname of the particular node.
@: Select attribute.
Attribute: Attribute name of the node.
Value: Value of the attribute
###
XPath Locators	Find different elements on web page
ID	---> To find the element by ID of the element
Classname  --->	To find the element by Classname of the element
Name  --->	To find the element by name of the element
Link text  --->	To find the element by text of the link
XPath  --->	XPath required for finding the dynamic element and traverse between various elements of the web page
CSS path  --->	CSS path also locates elements having no name, class or ID.
'''
