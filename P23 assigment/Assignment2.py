#Student Management System

class students():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display_details(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")



student1 = students("Laxmi", 19, 85)

student1.display_details()
student1.check_result()