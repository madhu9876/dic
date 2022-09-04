# my_dict = {'data1':100,'data2':-54,'data3':247}#dn
# print(sum(my_dict.values()))

# dict={'a':4,'b':-5,'c':9}
# print(sum(dict.values()))

dict={'a':4,'b':-5,'c':9}
sum=0
for i in dict:
    sum+=dict[i]

print(sum)
