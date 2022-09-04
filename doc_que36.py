key,value={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
for i,j in zip(key,value):
    if key[i]==value[j]:
        print(i,":1 is present in both key,value")



# a,b={'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# for k,v in zip(a,b):
#     if a[k]==b[v]:
#         print(k,": is present in both a,b")