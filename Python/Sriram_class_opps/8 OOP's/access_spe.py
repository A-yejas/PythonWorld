# All name variables and methods are public by default in Python

# Protected variable we can define By prefixing the name of your variable or method with a single underscore,
#you’re telling others “don’t touch this, unless you’re a subclass”

#  private variable we can define By prefixing the name of your variable with a double underscore,
#  By declaring your data member private you mean, that nobody should be able to access it from outside the class.


# class One():
#     name = 'public'     # public
#     _name = 'protect'   # protect
#     __name = 'Pravate'  # pravate
#
#     def _add(self):
#         print('Add is: 999 ' ,self.__sub())
#
#     def __sub(self):
#         return 'AAAAAA'
#
# ins = One()
# print(ins._name)
# ins.__sub()

'''
31/08/2024
In python every thing is an public, is availbel every where
# __Private :- Private things are not allowwed to access the out of the class but Private things basically allowed
# _Protect:-  prodtect available with in the modules to things in class.


'''

# class login:
#
#     def __init__(self,email,password,name):
#         self._email=email
#         self.__password = password
#         self.name = name
#     def allow_to_change(self):
#         if self._email=='yejas@gmail.com' and self.__password=="pwd@123":
#             print("allowed")
#         else:
#             print("not allowed")
#
# call=login('yejas@gmail.com', 'pwd@123', 'yejas')
# call.allow_to_change()
# print(list(call))


