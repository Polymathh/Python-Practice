sentence = input('Enter a sentence: ')

sentence = sentence.lower() #The  the

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print('\nWord Frequencies:')
for word, count in word_count.items():
    print(f'{word}: {count}')
