# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}##
# print("key value count")
# c=1
# for i in dict_num:
#     print(i,'  ',dict_num[i],'  ',c)
#     c+=1



dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key value count")
c=1
for i,j in dict_num.items():
    print(i," ",j," ",c)
    c+=1