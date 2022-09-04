List= [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict={}
for i in List:
    if i[0] not in dict.keys():
        dict.update({i[0]:[i[1]]})
    elif i[0]in dict.keys():
        dict[i[0]].append(i[1])
print(dict)



        
