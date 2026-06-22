# Polymorphism means "One thing, many forms."

# Same method name, but different classes can have different implementations. 
#ek hi naam ke difference work that is phnomeon of polymorphism

class  Animal:
    def speak(self):
        print("animal are speaking")

class Human:
    def speak(self):
        print("humans aree inteligent so they are speaking")

obj1=Animal()
obj2=Human()

obj1.speak()
obj2.speak()

# both the speak methods appears to the 
#same but both have different task and this is 
#known as polymorphism

class animal:
    def hello (self,a):
        print("how are you")

    def hello (self,a,b):
        print("how are you man")

#TYPES OF POLYMORPHISM
# 1. compile time polymorphism (method overloading) -> same method name but different parameters
# 2. run time polymorphism (method overriding) -> same method name but different implementation

#1. COMPILE TIME POLYMORPHISM (METHOD OVERLOADING) -> Note: Python does not support true method overloading like Java/C++
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c

# obj=Calculator()
# print(obj.add(2,3)) # This will cause an error because the second add method overwrites the first one
# print(obj.add(2,3,4)) # This will work and return 9

# 2. RUN TIME POLYMORPHISM (METHOD OVERRIDING) 
# ab child class parent class ke method ko same name aur same parameters ke saath dobara define karti hai, to ise Method Overriding kehte hain.
# Animal says: "I make a sound"
# Dog says: "I bark"
# Dog ek Animal hai, lekin uska sound alag hai. Isliye Dog parent ke method ko override karta hai.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound() # Output: Dog barks (not "Animal makes sound") because the Dog class has overridden the sound method of the Animal class.
"""Benefits of Polymorphism (Hinglish)
1. Code Reusability ♻️

Ek hi interface/method ko different classes ke saath use kar sakte hain.

2. Flexibility 🤸

Same method name different objects ke liye different behavior de sakta hai.

3. Easy Maintenance 🔧

Code ko update aur manage karna aasaan ho jata hai.

4. Better Readability 📖

Same method names use hone se code simple aur clean lagta hai.

5. Extensibility 🚀

Nayi classes add kar sakte hain bina existing code ko zyada change kiye."""

