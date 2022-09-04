list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dict={}
for i in list:
    a={i[0]:i[1:]}
    dict.update(a)
print(dict)