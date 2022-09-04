my_dict = {'x':500, 'y':5874, 'z': 560}#dn
print("maximum:",max(my_dict.values()))
print("minimum:",min(my_dict.values()))


# dict = {'sajib':20,'preetom':21,'showrov':22,'toha':23,'nazmul':24}
# print(max(dict.values()))
# print(min(dict.values()))

# dict= {"a" : 100,"b" : 200,"c": 50}
# print("Maximum value is", max(dict.values()), "and", "Minimum value is", min(dict.values()))


dict={}#dn
a=int(input("Enter a number of entries: "))
for i in range(0,a):
    b= int(input("Enter a number: "))
    dict[b]=b
print("Maximum of values is: ",(max(dict.values())))
print("Minimum of values is: ",(min(dict.values())))