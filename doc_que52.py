dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}#doubt
firstmaxval=[]
for i,j in sorted(dic.items(),key=lambda x:x[1],reverse=True):
    firstmaxval.append(i)
    break
print(firstmaxval)
twomaxval=[]
for i,j in sorted(dic.items(),key=lambda x:x[1],reverse=True):
    twomaxval.append(i)
print(twomaxval[:5])