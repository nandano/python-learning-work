pet_0 = {
    'name': 'doggo',
    'type': 'dog',
    'owner': 'peter',
}

pet_1 = {
    'name': 'catty',
    'type': 'cat',
    'owner': 'mithilesh',
}

pet_2 = {
    'name': 'gi',
    'type': 'giraffe',
    'owner': 'sanya',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    owner = pet['owner'].title()
    pet_type = pet['type'].title()
    pet_name = pet['name'].title()
    print(f"{owner} owns a {pet_type} named {pet_name}.")
