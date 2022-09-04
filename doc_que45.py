# list=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# # Remove id #FF0000 from the said list of dictionary:
# remove='#FF0000'
# result=[]
# for i in list:
#     if remove in i.values():
#         pass
#     else:
#         result.append(i)
# print(result)


list=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
{'id': '#FFFF00', 'color': 'Yellow'},{'id': '#808000', 'color': 'Olive'}]
a=[]
for i in list:
    if i['id']!='#FF0000':
        a.append(i)
print(a)
        