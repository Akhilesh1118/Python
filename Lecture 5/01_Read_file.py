# File I/O 
# Open, read &  close


f = open("sample.txt","r")  # file object. 

data = f.read()
# data = f.readline()   It print the first line of the txt file . 
print(data)

print(type(data)) 

f.close()


