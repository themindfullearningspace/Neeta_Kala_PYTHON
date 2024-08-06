#The difference between '==' and 'is' opeartor through an empty list
list1 = []
list2 = []
list3 = list1

print(id(list1))
print(id(list2))
print(id(list3))

if(list1 == list2):
  print("True")
else:
  print("False")
  
  
if(list1 is list2): #since the list1 and list2 have different id i.e. both the lists are at different memory locations, that's why it gives us the 'False' as output
  print("True")
else:
  print("False")
  
# The Equality operator (==) is a comparison operator in Python that compare values of both the operands and checks for value equality. 
# Whereas the 'is' operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).

if(list1 == list3):
  print("True")
else:
  print("False")
  

if(list1 is list3):
  print("True")
else:
  print("False")
  
list3 = list3 + list2

if(list1 is list3):
  print("True")
else:
  print("False")