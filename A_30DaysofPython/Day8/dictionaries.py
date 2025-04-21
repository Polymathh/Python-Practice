person = {
    'name':'Wambugu',
    'age':50,
    'city':'Nairobi',
}

#adding values
person['email'] = 'wambugu@gmail.com'

#Updating the values
person['age'] = '70'

print(person)

del person['city']
print(person)
