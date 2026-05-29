class student:
    subject = "Python"
    University = "MUIT"
    Year = "3th year"
stud1 = student()
print(stud1.subject, stud1.Year)

class students:
  def __init__(self, name ):
    #  print("constructer called automatically .")
        self.name = name # how to pass variable in to init function . 

std = students("Akhilesh") 

print(std.name)
