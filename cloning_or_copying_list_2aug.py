#We are cloning or copying a list: using 5 different ways
#1. Using the slicing technique

# def cloning(li1):
#   li_copy = li1[:]
#   return li_copy

# li1 = [4, 8, 2, 10, 15, 18]
# li2 = cloning(li1)
# print("Original Cloning: ", li1)
# print("After Cloning: ", li2)

#Extend Method()
#This appends each element of the iterable object(e.g. another list) to the end of the new list.
# def cloning(li1):
#   li_copy = []
#   li_copy.extend(li1)
#   return li_copy

# li1 = [4, 8, 2, 10, 15, 18]
# li3 = cloning(li1)
# print("Original Cloning: ", li1)
# print("After Cloning: ", li3)

#importing copy module
# import copy

# #intializing list 1
# li1 = [1, 2, [3, 5], 4]

# #using copy for shallow copy
# li2 = copy.copy(li1)

# #A shallow copy means that a new object is created, but the elements of 
# # the original object are not copied; instead, references to the objects are copied, copy(first copy )accesses the 'copy' module
# # the second copy is the function within the 'copy' function
# li2 = copy.copy(li1)
# print(li2)

# def cloning(li1):
#   li2 = [element for element in li1]
#   return li2

# li1 = [4, 8, 2, 10, 15, 18]
# li2 = cloning(li1)
# print(li2)

#Here, the first i: This is the element that will be included int he new list 'li2'
# the second i: THis is the iteration variable that takes on each value in the list 'li1' as the list comprehension iterates over it.

#PYthon append() to clone or copy a list
def clone(list1):
  li_copy = []
  for item in list1:
    li_copy.append(item)
  return li_copy
  
li1 = [4, 8, 2, 7, 9, 11]
li2 = clone(li1)
print(li2)