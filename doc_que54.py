dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
list=[]
for i,j in dict.items():
    for key in j:
        a={i:key}
        list.append(a)
print(list)