class student:
      college_name = "MUIT" # CLASS ATTRIBUTES 

      def __init__(self, name, cgpa): # INSTANCE ATTRIBUTS. 
        self.name = name
        self.cgpa = cgpa 

    # def get_cgpa(self):
    #     return self.cgpa
    

stud1 = student("Akhilesh", 9.9)
stud3 = student("Bhishmdutt", 8.4)
stud2 = student("kuldeep ", 7.4)

# in the method 

# print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}" )

print(stud1.name)