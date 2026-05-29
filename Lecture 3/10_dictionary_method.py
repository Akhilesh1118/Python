# Methos 
# d.keys()  return all key 
# d.values() return all values
# d.items() return (key, value) in pairs
# d.get(val) return val acc. to key 
# d.update(new_dict) adds new item to dict.

info = {
    "name" : "Akhilesh",
    "subject" : ["math","english"],
    "score":99,
    3.14:"PI"
}

# type casting into list 
print(info.items())


dict_key = list(info.keys())
print(dict_key)

# update
info.update({
    "city" : "Noida",
    "course" : "B.tech"
})

print(info)