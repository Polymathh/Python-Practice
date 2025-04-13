names = []

#loop to collect names
for i in range(3):
    name = input('Enter a name: ')
    names.append(name)

#Show all names
print('You entered:' , names)

for name in names:
    print("Hello", name)