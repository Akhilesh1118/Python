# # Nested condition 
# if -- if only used by the indivisual 
# elif  they are not use in indivisual they work only with if condition first. 
# else indivisual wrong. 

"""
age = int(input("enter age: "))

if(age < 13):
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")

basic example of login page. 
"""

username = input("enter username : ")
password = input("enter password : ")

if (username == "admin" and password == "pass"):
    print("Login Successfully ")
elif (username != "admin"):
    print("Wrong username")
else:
    if ( password != "pass" ):
        print("Invaild credintional ")