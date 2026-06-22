#opps 
# OOPS (Object-Oriented Programming System) is a programming approach that 
# organizes code using classes and objects.
# Class → Blueprint for creating objects.
# Object → Instance of a class.
# 18 may 2026
#class in store only two things attributes and methods
class factory:
    a=10#class variable/attribute
    def menu(self):#method
        print("This is menu method")
print(factory.a)#accecing attributes(They are accessed using the dot)
factory.menu(factory)#accesing method

class hello:
    def speak(self):
        print(self)
        print("how are you")
obj=hello()#created an object
print(obj.a)#Object dot (.) operator ki help se attributes aur methods access karta hai.
# Jab object kisi method ko call karta hai,
obj.speak()# Python automatically object ka reference self me pass kar deta hai. ✅



class SharmeVishnu :# class is a object of bluprint
    def sample():
        print("This is sample")
SharmeVishnu.sample()
OR
def sample2():
    print("This is sample2 function ")
SharmeVishnu.sample()
print(SharmeVishnu.a)

# class ke function create krne ko method khte hai
# class ke ander variable print ko atrributes khte hai 


# ki jab bhi class ke aunder ke function ko object ki help se \
#  call karoge toh ek parameter set kerna hoga
# object ka naam same as hota hai as name of the variable
# chacha =Animal()# here chacha is object. 
# create a class ywhitcg  will perdorm  2 task 
# 1.greet the user-
# 2.adding up two  numbers
class Baggah :
    def greet (self):
        print("hello from baggah class")
        def add (self):
            a=10
            b=10
            print(a+b)

class baggah:
    obj=Baggah ()
    obj.greet ()
    obj.add()
# python me second line execute honta
# constructor is a special method which is used to initialize the object of the class
# constructor  -->represented by __init__(dunder method) 
# constructor  sabse pahle excute hone wale function hai  dosent matter inke upar ya neeche  koi bhi 
# function present hai 

# class SharmaVishnu:
#     def __init__(self, name,age):
#             self.name=name#instance variable/attribute
#             self.age=age
#     print("This is constructor")
    

#    object ka naam same as hota hai as name of the variable
#    chacha =Animal()# here chacha is object. 
# create a class ywhitcg  will perdorm  2 task 
# 1.greet the user-
# 2.adding up two  numbers
# class Baggah :
    def greet (self):
        print("hello from baggah class")
        def add (self):
            a=10
            b=10
            print(a+b)

class baggah:
    obj=Baggah ()
    obj.greet ()
    obj.add()
# python me second line execute honta
# constructor is a special method which is used to initialize the object of the class
# constructor  -->represented by __init__(dunder method) 
# constructor  sabse pahle excute hone wale function hai  dosent matter inke upar ya neeche  koi bhi 
# function present hai 
class SharmaVishnu:
    def __init__(self, name,age):
            self.name=name#instance variable/attribute
            self.age=age
    print("This is constructor")
    

#    object ka naam same as hota hai as name of the variable
#    chacha =Animal()# here chacha is object. 
# create a class ywhitcg  will perdorm  2 task 
# 1.greet the user-
# 2.adding up two  numbers
class Baggah :
    def greet (self):
        print("hello from baggah class")
        def add (self):
            a=10
            b=10
            print(a+b)

class baggah:
    obj=Baggah ()
    obj.greet ()
    obj.add()
# python me second line execute honta
# constructor is a special method which is used to initialize the object of the class
# constructor  -->represented by __init__(dunder method) 
# constructor  sabse pahle excute hone wale function hai  dosent matter inke upar ya neeche  koi bhi 
# function present hai 
class SharmaVishnu:
    def __init__(self, name,age):
            self.name=name#instance variable/attribute
#             self.age=age
#     print("This is constructor")
    

   # object ka naam same as hota hai as name of the variable
# #    chacha =Animal()# here chacha is object. 
# // create a class ywhitcg  will perdorm  2 task 
# // 1.greet the user-
# // 2.adding up two  numbers
# // class Baggah :
# //     def greet (self):
# //         print("hello from baggah class")
# //         def add (self):
# //             a=10
# //             b=10
# //             print(a+b)

# // class baggah:
# //     obj=Baggah ()
# //     obj.greet ()
# //     obj.add()
# // python me second line execute honta
# //constructor is a special method which is used to initialize the object of the class
# //constructor  -->represented by __init__(dunder method) 
# // constructor  sabse pahle excute hone wale function hai  dosent matter inke upar ya neeche  koi bhi 
# // function present hai 
# // class SharmaVishnu:
# //     def __init__(self, name,age):
# //             self.name=name#instance variable/attribute
# //             self.age=age
# //     print("This is constructor")
    

#    // object ka naam same as hota hai as name of the variable
# //    chacha =Animal()# here chacha is object. 
# // create a class ywhitcg  will perdorm  2 task 
# // 1.greet the user-
# // 2.adding up two  numbers
# // class Baggah :
# //     def greet (self):
# //         print("hello from baggah class")
# //         def add (self):
# //             a=10
# # //             b=10
# //             print(a+b)

# // class baggah:
# //     obj=Baggah ()
# //     obj.greet ()
# //     obj.add()
# // python me second line execute honta
# //constructor is a special method which is used to initialize the object of the class
# //constructor  -->represented by __init__(dunder method) 
# // constructor  sabse pahle excute hone wale function hai  dosent matter inke upar ya neeche  koi bhi 
# function present hai 

# obj.menu()
# jo obj create karte hai ase object ko instance bhi kehte hai
# make a class which will takes 2 numbers as input  create
# 1 . instant AttributeError
# 2. method which will print greatest among them
# class Greatest:
#     def __init__(self, a,b):
#         self.a=a
#         self.b=b
#     def greatest(self):
#         if self.a>self.b:
#             print(f"{self.a} is greater than {self.b}")
#         elif self.b>self.a:
#             print(f"{self.b} is greater than {self.a}")
#         else:
#             print("Both numbers are equal")

# # Example usage:
# obj = Greatest(10, 20)
# obj.greatest()
# # 20 may 2026
