# Definition

# Inheritance ek OOP concept hai jisme ek class dusri class ke attributes aur methods ko inherit (receive) karti hai.
# Parent Class / Base Class → Jiski properties inherit hoti hain.
# Child Class / Derived Class → Jo properties inherit karti ha







class Bhopalfactory :#(parent class)
    def __int__(self,color ,size,type):
        self.color=color
        self.size=size
        self.type=type
    def details(self):
        self.color
        self.size
        self.type
class indorefactory(Bhopalfactory):#child class
    def __init__(self,color,size,type,price):
        super().__init__(color,size,type)
        self.price=price
class ujjainfactory (indorefactory):#multilevel inheritence
    def __init__(self, color, size, type, price):
        super().__init__(color, size, type, price)


shoe1=Bhopalfactory("red",8,"jorden")
shoe2=indorefactory("yellow ",7,"sneakers",10000)
shoe2.details()

# Super Easy Memory Trick

# Single = 1 Parent → 1 Child
# Multiple = Many Parents → 1 Child
# Multilevel = Chain 🔗
# Grandfather → Father → Son
# Hierarchical = 1 Parent → Many Children
# Hybrid = Mix 🔀
# Hierarchical + Multiple

# SINGLE INHERITENCE → 1 Parent → 1 Child:
class Animal:# parent class
    def eat(self):
        print("eating")
class Dog(Animal):# child class
    def bark(self):
        print("barking")
obj=Dog()    
obj.eat()#
obj.bark()
# MULTIPLE INHERITENCE → Many Parents → 1 Child:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):#child class jo dog aur animal dono se inherit kar raha hai
    def weep(self):
        print("Weeping")

obj = Puppy()

obj.eat()
obj.bark()
obj.weep()

# MULTILEVEL INHERITENCE → Chain 
class grandfather:
    def eat(self):
        print("greeting good morning")

class Father(grandfather):#child class jo grandfather se inherit kar raha hai
    def greet(self):
        print("greeting good afternoon")

class son(Father):#child class jo father se inherit kar raha hai
    def greet(self):
        print("greeting good evening")

obj=son()
obj.greet()

# HIERARCHICAL INHERITENCE → 1 Parent → Many Children
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()
# HYBRID INHERITENCE → Mix
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

class Puppy(Dog, Cat):
    pass

obj = Puppy()

obj.eat()
obj.bark()
obj.meow()












# class A :    #super parent class
#      def greet(self):
#          print("this is class A")
         
# class B(A):   #parent class
#     def show(self):
#         print("this is class B")
        
# class C(B):   #child class
#     def details(self):")

# obj = Child()
# obj.show()
# obj.greet()

#   EXAMPLE 2

# class CEO:# super parent class
#     def __init__(self):
#         print("this is CEO class constructor")

# class Manager(CEO): #child class /parent of employ
#     def __init__(self):
#         super().__init__()
#         print("this is manager class constructor")

# class Employee (Manager):# 
#     def __init__(self):
#         super().__init__()#parent class ke attribute lane ho toh 
#         print("this is employ  class constroctor")

# rahul=Employee()

# 4. herachical inheritence ->1 parent and multiple child
# class parent :
#     def greet (self):
#         print("this is parent class ")

# class  child1(parent):
#     pass

# class child2(parent):
#     pass

# obj=child2()
# obj.greet()

# obj2=child1()
# obj .greet ()

# Q.2
class  Account :
    def __init__(self,name,balance):
        self.balance

    def details(self):
        print(f"Hello {self.name}you have {self .balance}")

class saving (Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        
        print(f"this is saving class constrctor{self.name},{self .balance}")

    class current (Account):
        def __init__(self, name, balance):
            super().__init__(name, balance)
            self.type =type
            print("this is current class cunstroctor")

    obj =current("mukesh ",0,"current")

