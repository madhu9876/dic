# count = {"M":0,"I":0,"S":0,"P":0}#dought
# word = "MISSISSIPPI"
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	elif i == "P":
# 		count['P'] = count['P']+1
# print(count)


# word = "MISSISSIPPI"
# count=0
# dict={}
# for i in word:
# 	if i == "M":
# 		count= count+1
# 	elif i == "I":
# 		count= count+1
# 	elif i == "S":
# 		count = count+1
# 	elif i == "P":
#         count = count+1
    
# print(count) 



str1 = 'MISSISSIPPI'#dn
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter,0)+1
print(my_dict)