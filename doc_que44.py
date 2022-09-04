# dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# result=[dict(zip(dic.keys(),items)) for items in list(zip(*dic.values()))]
# print(result)

#op-[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62,'Language':84}, {'Science': 95, 'Language': 80}]
dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}#doubt
list=[]

key,value=dic.values()
for i in range(len(key)):
    for j,k in dic.items():
        value=({j:k[i]})
        list.append(value)
print(list)

