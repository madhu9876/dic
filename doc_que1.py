d1={'a':100,'b':200,'c':300}#dn
d2={'a':300,'b':200,'d':400}
dict={}
for i in d1:
    for j in d2:
        if i in d2:
            dict[i]=d1[i]+d2[i]
        elif j not in d1:
            dict[j]=d2[j]
        elif i not in d2:
            dict[i]=d1[i]
print(dict)





