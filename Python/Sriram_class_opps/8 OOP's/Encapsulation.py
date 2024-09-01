#Encapsulation is wrapping data or functionality(methods accessing data) together into single uint.

#Giving protection to the class or class members. Using access specifiers/modifiers we can achive it.

# class One():
#     name = 'public'     # public
#
#     def __init__(self, a):
#         self.a = a
#
#     def add(self):
#         print('sum is ')
#
#     def __sub(self):
#         print('sub is:')
#         cls._add()
#
# ins = One(3)
# print('\n ', ins.name)
# Quick Two Line Codes
countOfWords = len("Geeksforgeeks is best Computer Science Portal".split())
print("Count of Words in the given Sentence:", countOfWords)

# Quick One Line Codes
print(len("Geeksforgeeks is best Computer Science Portal".split()))

# Quick One Line Code with User Input
print(len(input("Enter Input:").split()))
'''
31/08/2024:-

In python every thing is an public, is availbele every where
# __Private :- Private things are not allowwed to access the out of the class but Private things basically allowed
# _Protect:-  prodtect available with in the modules to things in class.
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

'''
