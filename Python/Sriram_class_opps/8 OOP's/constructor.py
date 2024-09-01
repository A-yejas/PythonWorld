## Uusing constructor we can create instance varables.
# class One():
#     def __init__(self):
#         pass
#     def add(self, uname, password):
#        print('\n ADD ', uname , password)
#
#     def sub(self, uname, password, hostname,port):
#         print(uname, password )
#
#     def mul(self, uname, password):
#         print(uname, password )
# inst = One()
# inst.add(10,20)
# inst.sub(10,20,'admin', 23)
# inst.mul(10,20)

# class One():
#     def __init__(self, uname, password):
#         self.uname = uname
#         self.password = password
#         print('__INIT__')
#
#     def add(self):
#        print(self.uname , self.password)
#
#     def sub(self, hostname,port):
#         print(self.uname, self.password )
#
#     def mul(self):
#         print(self.uname, self.password )
#
# inst = One('admin','admin123')
# inst.add()
# inst.sub('admin', 23)
# inst.mul()
'''Udemy Step by step'''
'''
1.constructor is one method which is automatically called when you create object for any class.
2.Class varaiable & instance variables have whole different purpose
4.Constructor name should be __init__
5. self is like global and universal to call any variable.
6.but for class variables you have provision as it is class variable, you can use calculator.num or self.num
7.Self keyword is mandatory for calling variaable names into method

'''
class Calculator:
    '''
    whatever variable you define immediately inside your class are nothing but class variables.
    '''
    num = 100
    def __init__(self,a,b):    #and the variables which you define inside constructor are called instance variables.
        print("i am getting called automatically")
        self.Firstnum = a
        self.Secondnum = b
    def getData(self):
        print('i am now executing as the method now')

    '''
     you can never call a variable simply with its name. like [Firstnum + e.t.c.,.]
     You have to always attach with the self dot.
     Here self is nothing but object reference of who is calling you.
    '''
    def summation(self):

        return self.Firstnum + self.Secondnum + Calculator.num

obj=Calculator(2,3)
obj.getData()
obj.summation()
print(obj.num)
print(obj.summation())

'''
31/08/2024
1.Constructor is a special method which is invoked automatically at the time of object creation.
# 2.it is used to initilize the data members of the new objects generally.
# 3.Constructors have the same name as class or structure.
# 4.Constructor dont have a return type.(Not even void).
# 5.Constructor are only called once, at object creation.
# def __init__()   ->default constructor
# Constructor which has parameters is called a parameterized constructor.it is used to provide different values&distinct objects
# def __init__(self,name,id)  --> parameterize constructor

'''
# class Student:
#
#     def __init__(self):
#         print(">>>>>>>>>")
#         self.name = input("Enter the name")
#         self.age = input("Enter the age")
#
#
#     def display(self):
#         print(f"The name is {self.name}, and age is {self.age}")
#
# obj = Student()
# obj.display()
#####
# class login:
#     def __init__(self,email,pwd):
#         self.email=email
#         self.pwd=pwd
#     def login_allow(self):
#         if self.pwd == 'pwd123':
#             print("Allowed")
#         else:
#             print('Not allowed')
# object=login('yejas', 'pwd1234')
# object.login_allow()
# object1=login('Noor','pwd123')
# object1.login_allow()
