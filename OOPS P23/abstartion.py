#ABSTRACTION 
#Abstraction is the process of hiding the internal details of an object and only exposing a public interface. It is one of the fundamental principles of object-oriented programming (OOP) and helps to protect the data and ensure that it is used in a controlled manner.
# User ko "What to do" pata hota hai, lekin "How it works internally" hidden rehta hai.

"""Why Use Abstraction?
1. Hides Complexity 🎭

User ko sirf required features dikhte hain.

2. Improves Security 🔒

Internal logic hidden rehta hai.

3. Better Code Organization 📂

Code clean aur structured hota hai.

4. Reduces Redundancy ♻️"""


#Python mein abstract method ek aisa method hota hai jiska sirf declaration hota hai, implementation nahi hoti. Child class
# ko us method ko implement karna mandatory hota hai.

# from abc import  ABC ,abstractmethod

# class shapes (ABC):
#     @abstractmethod
#     def area ():
#         pass

#     @abstractmethod
#     def perimeter():
#         pass
# class square(shapes):
#     def __init__(self,side):
#         self.side =side

#     def perimeter (self):
#         print(4*self.side)

#     def area(self):
#         print(self.side *self.side)

# class circles(shapes):
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area ():
#         pass
#     def perimeter():
#         pass 
# obj=square (10)
        
#DUNDER METHOD(MAGIC METHOD)# DUNDER METHODS are special methods in Python that have double underscores at the beginning and end of their names. They are also known as magic methods or special methods. These methods allow you to define how objects of a class behave with
# built-in operations and functions. For example, __init__ is a dunder method that initializes an object when it is created, and __str__ is a dunder method that defines how an object is represented as a string.

# class Robots:
#     a=12
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return f"hello my name is {self.name}"


# obj1=Robots("alpha1")
# obj2=Robots("beeta1")

# print(obj1)
#COMPARISION OPERATOR
class Numbers:
    def __init__(self,value):
        self.value=value

    def _add_(self,other): #addition method 
        return self.value +other.value
    
    def __eq__(self, value):# magic methods
        return self.value ==value.value 
    
a= Numbers(20)
b=Numbers(30)

print(a==b)






    