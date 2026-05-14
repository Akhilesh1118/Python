username = input("enter username : ")
password = input("enter password : ")

if (username == "admin" and password == "pass"):
    print("Login Successfully ")
else:
  if(username != "admin"):
      print("Wrong username")
  else:
        print("Wrong password.")