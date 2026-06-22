# Encapsulation is the process of hiding the internal details of an object and only exposing a public interface.
# It is one of the fundamental principles of object-oriented programming (OOP) and helps to
# protect the data and ensure that it is used in a controlled manner.
#Isse Data Hiding bhi kehte hain.

#Types of Encapsulation:
#Public	name	Anywhere
# Protected	_name	Class & Child Class (by convention)
# Private	__name	Only inside same class
class Animal:
    name="lion"# public attribute
    _age =12 # protected attribute
    __height=120# private attributes
    @classmethod
    def  speak (self):#public object method
        print("the lion roars")

    def _walk(self):#protected object method
        print("the lion is walking")


    def __sleep (self):# private method
       print("the lion is sleep")
     
obj1=Animal()
print (obj1.name)
# obj1.__sleep

# private attributes and methods cannot be accessed by your objects and 
#inherited classes