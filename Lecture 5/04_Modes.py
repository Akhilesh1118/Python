# File Operations 
# Modes 

# r  reading [default]
# w  writing, truncates file first
# x  creates new & open for writing 
# a  writing , appends at end 
# b  binary mode 
# t  text mode [default ]
# +   opens disk file for updater (r  & w )

f = open("sample.txt" , "a") # file object 
# \n  use to give the next line 
f.write("\n New text being appended \n to the file ")

f.close()