person_0 = {
    'first_name': 'jack',
    'last_name': 'jackie',
    'age': 23,
    'city': 'new york'
}

person_1 = {
    'first_name': 'brock',
    'last_name': 'lesnar',
    'age': 40,
    'city': 'new york'
}

person_2 = {
    'first_name': 'marvin',
    'last_name': 'gaye',
    'age': 30,
    'city': 'washington d c'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()} lives in {person['city'].title()} and is {person['age']} years old.")
