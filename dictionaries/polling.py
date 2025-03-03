favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

take_poll = ['jen', 'edward', 'rajesh', 'al khwarizmi', 'maxwell']

for person in take_poll:
    if person in favorite_languages.keys():
        print(f"{person.title()} thank you for responding.")
    else:
        print(f"{person.title()}, please take the poll.")
