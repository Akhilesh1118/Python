# Exception Handling. 
# try, except, else, finally 

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed..")

except ValueError:
   print(f"Invalid inputadfa")
else:
 print(f"ans = {ans}")

finally:
   print("End of program .")