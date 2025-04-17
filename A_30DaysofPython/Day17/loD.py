users = [
    {'name': 'Wambugu', 'age': 50},
    {'name': 'John', 'age': 52},
]

print(users[0]['name'])

for user in users:
    print(f"{user['name']} is {user['age']} years old")