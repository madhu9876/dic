a=int(input("how many students:-"))#dn
b={}
for i in range(0,a):
    c=input("students name:-")
    d=int(input("marks:-"))
    b.update({c:d})
print(b)