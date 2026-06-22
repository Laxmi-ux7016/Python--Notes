#CONSTRUCTOR
#20 may 26
# 1. Classmethod
#2. Staticmethod
#3.object method

# | Method Type   | First Parameter | Access                          |
# | ------------- | --------------- | ------------------------------- |
# | Object Method | `self`          | Instance Variables              |
# | Class Method  | `cls`           | Class Variables                 |
# | Static Method | None            | Neither instance nor class data |


# instance attribute kbhi bhi class attribute ko change nhi kr skta hai   
#constructor is a special method which is used to initialize the object of the class
# class factory:
#     def __init__(self):#constructor function is called 
#          print("how are you")
#     print("this is p23 batch")

# a=factory()#object
# b=factory()#object
# c=factory()#object
#2nd use of constructor function
class  factory:
    def _init_(self,zips,pocket,material):
        self.zips=zips
        self.pocket=pocket
        self.material=material
    def details(self):
        print("your bag details are:- ")
        print(self.zips)
        print(self.pocket)
        print(self.material)

reebok = factory(2,2,"leather")#object
campus = factory(3,4,"plastic")#object  
reebok.details()
print(campus.material)

class Registration:
    age=18#class attribute
    def _init(self ,name,email,age ,number):
        if age>= Registration.age:
            self.name=name#object attribute
            self.email=email
            self.number=number
        else:
            print("your cannot register you are underage")
            return
    def  details (self):#object method-it target the location of  objects or instance
        print(self.name)#self will take the location of the objects
        print(self.email)
        print(self.number)
        print(self.age)

    @classmethod
    def dummy_details(cls):# class method -it will always access the location of your class
        print(cls.name)
        print(cls.email)
        print(cls.number)
        print(cls.age)
    @staticmethod
    def college_details():
        print("i am aa very bad college i will take your money  and i will not teach you anything welcome to real world")

student1=Registration("harsh","harsh@gmail.com")

##revision 3

        

# class Animal:#class
#     name="Dog"#class attribute
#     #instance (object )can never change your  class attribute
#     @classmethod#decorator
#     def change (cls,new):#cls ->object
#         cls.name=new#class attribute ko change krne ke liye class method ka use krte hai
#         print(cls.name)

#         cheeta=Animal()#object
#         cheeta.change("cat")#class method ke through class attribute ko change kr diya
#         print(Animal.name)
#2. Static method

# class SharmaVishnu:
#     @staticmethod#independent of object ,means object may create or not 
#     def manu():
#         print("Paneer Kulche")
#         print("pizza")
#         print("pannr cheeze sandwich")
#         print("Cold coffee")

# new_market=SharmaVishnu()#object
# new_market.manu()#static method ko call krne ke liye object ka use krte hai

#21 may 2026

#INHERITENCE
#Types of inheritence
#1. single inheritence
#2. multiple inheritence
#3. multilevel inheritence
#4. hierarchical inheritence
#5. hybrid inheritence

#1. single inheritence
# class Parent:
#     def __init__(self):
#         print("This is parent class constructor")
#     def greet (self):
#         print("this is parent class")

# class child (Parent):
#     def __init__(self):
#        print("this is child class constructor") 
#     def show (self):
#         print("this is child class")

# obj=child()
# obj.greet()
# obj.show()

# class factory:
#     def __init__(self):
#         print("This is factory class constructor")
#         self.name= name
#         self.color=color

#         def show (self):
#             print(f"bag has {self.name} and {self.color}")  


# Multiple  Inheritance 2 parent 1 child
class father :#parent1
    def greet_father(self):
        print("this is father class")

class mother :#parent2
    def greet_mother(self):
        print("this is mother class")

        class Child(father ,mother):#child class
            def greet_child(self):
                print("this is child class")

obj = Child()
obj.greet_father()
obj.greet_mother()

      
