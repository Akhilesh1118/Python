# Linear Sreach . 

num = [1,2,3,4,20]

# for i in num:
#     print(i)

x = 20
idx = 0

for val in num:
    if(val == x):
        print(f"{x} found at idx = {idx}")
        break
    idx = idx+1