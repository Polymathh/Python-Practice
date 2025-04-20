fruits = {'apple', 'banana', 'cherry'}
# print(fruits)

fruits.add('orange')
fruits.remove('apple')
fruits.discard('banana')
print(len(fruits)) #output 3

# fruits1 = {'Apple', 'banana'}
# fruits2 = {'cherry', 'orange'}

# allFruits = fruits1|fruits2
# print (allFruits)

fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"cherry", "apple", "grape"}
intersection_fruits = fruits1 & fruits2
print(intersection_fruits)  # Output: {'apple', 'cherry'}
