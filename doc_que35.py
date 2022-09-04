# dict= {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# for i,j in dict.items():
#     print(i,":",len(j))


# dict= {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# sum=0
# for i,j in dict.items():
#     sum+=len(j)
# print("count:",sum)

dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
print(sum(len(j) for i,j in dict.items()))
