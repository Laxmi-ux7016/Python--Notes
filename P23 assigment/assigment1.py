# STUDENT ADMISSION STATEMENT assigment1
    
class student:
    def __init__(self,name,age,email,phone_number):# Constructor function.
# Object banate time automatically call hota hai.
        self.name = name
        self.age = age # User ki details object ke andar store ho rahi hain.
        self.email = email
        self.phone_number = phone_number
        
    def display_details(self): #details show karne ke liye method banaya.
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.phone_number)
        
class class10admission(student): #student class ko inherit kar rahi hai
    def __init__(self,name,age,email,phone_number):
        super().__init__(name,age,email,phone_number)
        
        print("Admission successful")
    
class class12admission(student):
    def __init__(self,name,age,email,phone_number):
        super().__init__(self,name,age,email,phone_number)
        
        if self.age >= 16:
            print("admission successful")
        else:
            print("admission failed")
            
print("press 1 for class 10th admission")
print("press 2 for class 12th admission")

choice = int(input('enter your choice:- '))
name = input("tell your name:- ")
age = int(input('tell your age:- '))
email = input('tell your email:- ')
phone_number = input('tell your phone number:- ')

if choice == 1:
    student1 = class10admission(name,age,email,phone_number)
    student1.display_details()
    
if choice == 2:
    student1 = class12admission(name,age,email,phone_number)
    student1.display_details()

