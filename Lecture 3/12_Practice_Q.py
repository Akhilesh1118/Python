# Student Enrolments
# Given a list of tupes with info(name, subject ):

# 1. List all unique course.
# 2. List students enrolled in English
# 3. create dictionary (student, set of courses.)

info = [
    ("Alice","Math"), 
    ("Bob","Science"), 
    ("Alice","Science"), 
    ("Charlie","Math"), 
    ("Bob","Math"), 
    ("Alice","English"), 
    ("Charlie","English"), 
]

unique_courses = set()
for tup in info:
    unique_courses.add(tup[1]) # course. 

print(unique_courses)

# Q2
for name,course in info:
    if(course == "English"):
     print(name)

# Q3


dict = {}
for name, course in info:
   if(dict.get(name)==None):
      dict.update({name : set()})
      dict[name].add(course)
   else:
      dict[name].add(course)
print(dict)


