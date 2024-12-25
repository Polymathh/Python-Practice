# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

userInput = input('Enter integers separeted by space: ')
nums = [int(x) for x in userInput.split()]
totalSum = sum(nums)

print(f'The total sum is:',totalSum)