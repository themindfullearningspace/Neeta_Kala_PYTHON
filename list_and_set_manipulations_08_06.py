# list1 = ["Alice", "Bob", "Charlie"]
# print(" , ".join(list1))#join() function will join the given string from 1 to n-1 elements of any iterable object

# my_set= {1, 2, 2, 8, 1009, 90,3, 4, 5, 0}
# print(my_set)

# #Creating a set with
# #the use of a string
# set1 = set("GeeksForGeeks")
# print(set1)

# set1 = set("You are a geek")
# print(set1)

set1 = set([1, 2, "Geek", 3.14, (1, 2, 3), "for", "Geeks"])
print(set1)

set1 = set(["Geeks","for", "in", "Geeks"])
print("\nInitial set ")
print(set1)

print("\nElements of set: ")
for i in set1:
  print(i, end=" ")
  
#Checking the element
#using in keyword
print("Geeks" in set1)