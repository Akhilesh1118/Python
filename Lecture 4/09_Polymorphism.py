# Polymorphism - Many forms like + operator which is use for sum and also concatenate two string.
     
# 1. Function overriding 
# 2. Duck Typing. 


class Employee: 
    def get_designation(self):
        print("designation = Employee. ")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher ") 

t1= Teacher()
t1.get_designation()     # Over ride the function of Employee class. 