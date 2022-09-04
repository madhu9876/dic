dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict={}
for key,value in dict.items():
    if value!=None:
        new_dict[key]=value
print(new_dict)