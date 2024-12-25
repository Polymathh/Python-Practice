# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

input1 =input('Enter your first set of integers, separating them by spaces: ')
set1 = set(map(int, input1.split()))

input2= input('Enter your second set of integers, separating them by spaces: ')
set2 = set(map(int, input2.split()))

commomElements = set1.intersection(set2)

if commomElements:
    print(f'Common Elements:', commomElements)
else:
    print(f'No common elements found')

