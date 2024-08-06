#Creating an empty dictionary
dict1 = {}
print("Empty Dictionary: ")
print(dict1)

dict1 = {1:"Geeks", 2:'For', 3:"Geeks"}
print("\nDictionary with the use of Integer keys: ")
print(dict1)

dict1 = {'Name': 'Geeks', 1:[1, 2, 3, 4]}
print("\nDictionary with the use of Mixed keys: ")
print(dict1)
print(dict1['Name'])


dict1= dict({1: 'Geeks',
             2:'For',
             3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(dict1.get(3))

dict1 = dict([(1,'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(dict1)

a = 100 **100
print(a)

b = 9/3
print(b)

b = 9//3
print(b)