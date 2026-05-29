# Inheritance types. 
# 1. Single level Inheritance 
# 2. Multi level  
# 3. Multiple inher.

# exapmle of 2 level 
  
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role) # use super keword call the super class that create before this class. 
        self.salary = salary

acc1 = Accountant(25_000, "CA")

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)