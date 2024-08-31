'''
The differences between Assert and Verify are listed below −

Assert
1) Verifies if the specified condition is true and false.
If the result is true, the next test step will be executed. In case of false condition, the execution would terminate.
2.)In case of false condition, the next text case of the suite will be executed.
3) There are two types of assets namely hard and soft asserts.
Verify
1) Verifies if the specified condition is true and false. If the result is true,
the next test step will be executed. In case of false condition, the execution would still continue.
2) In case of false condition, the next test step of the same text case will continue.
3) There are no categories for verification.
'''

'''
Find element & Find elements:

findElement: A command used to uniquely identify a web element within the web page.
findElements: A command used to identify a list of web elements within the web page.

###
 Difference between findElement and findElements
 
## findElement	
1)Returns the first matching web element if multiple web elements are discovered by the locator.
2)Throws NoSuchElementException if the element is not found
3)Detects a unique web element

## findElements
1)Returns a list of multiple matching web elements
2)Returns an empty list if no matching element is found
3)Returns a collection of matching elements

'''