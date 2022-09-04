

dict= {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
new_dict= {}
for i,j in dict.items():
    for x in " ":
        i = i.replace(x,"")
    new_dict[i]= j
print(new_dict)




# d={'m adhu':['3','4'],'m ahi':['4','27']}
# dict={}
# for i,j in d.items():
#     for x in " ":
#         i=i.replace(x,"")
#     dict[i]=j
# print(dict)


