# dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for key in dict.keys():
#     dict[key]=[]
# print(dict)


dic={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
list=[]
for key,value in dic.items():
    if len(value)>0:
        a=key,[]
        list.append(a)
print(dict(list))