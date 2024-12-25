# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = input("Enter a list of words, separated by spaces: ").split()

oddWords = [word for word in words 
            if len(word) % 2 != 0]
print (f'Words with odd length:', oddWords)

