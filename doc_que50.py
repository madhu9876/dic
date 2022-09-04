# dict= {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print([[key,value] for key,value in dict.items()])

def test(dict):#doubt
    result = list(map(list, dict.items()))
    return result 
color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
#print("\nOriginal Dictionary:")
#print(color_dict)
#print("Convert the said dictionary into a list of lists:")
print(test(color_dict))