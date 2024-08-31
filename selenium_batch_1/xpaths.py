# 2 type of xpaths
'''
Absolute XPath
Relative XPath

Absolute XPath:
It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then
that XPath gets failed.

The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.

Absolute xpath example : /html/body/div[3]/div[2]/div/h4[4]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
####
Relative xpath:
Relative Xpath starts from the middle of HTML DOM structure. It starts with double forward slash (//).
It can search elements anywhere on the webpage, means no need to write a long xpath and you can start from the middle of
HTML DOM structure.
Relative Xpath is always preferred as it is not a complete path from the root element.
Relative XPath examle: //div[@class='featured-box cloumnsize1']//h4[1]//b[1]
###################
Basic X-path ex: Xpath=//input[@id='flask']
Xpath=//input[@type='txt']
Xpath=	//label[@id='msg22']
Xpath=	//input[@value='Submit']
Xpath=//*[@class='brony']
Xpath=//a[@href='http://selenium.org/']
Xpath= //img[@src='//guru99.com/images/home/java.png']
Xpath =  //*[text() = "Flights"]
#########
Contains (): Contains() is a method used in XPath expression.It is used when the value of any
attribute changes dynamically,
contains () xpath example: Xpath=//*[contains(@type,'sub')]
Xpath=//*[contains(@href,'selenium.com')]
Xpath=//*[contains(text(),'text')]
'''
#####
'''
**What are different types of frameworks?
Data Driven Framework:-
When the entire test data is generated from some external files like Excel, CSV, XML or some database table, then it is called Data Driven framework.
Keyword Driven Framework:-
When only the instructions and operations are written in a different file like an Excel worksheet, it is called Keyword Driven framework.
Hybrid Framework:-
A combination of both the Data Driven framework and the Keyword Driven framework is called Hybrid framework.
####
**Which files can be used as data source for different frameworks?
Some of the file types of the dataset can be: excel, xml, text, csv, etc


'''