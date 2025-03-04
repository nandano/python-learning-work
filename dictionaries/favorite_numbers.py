favorite_numbers = {
    'jack': [6],
    'rose': [9],
    'john': [15, 100],
    'albert': [37, 137],
    'erwin': [1, 19],
}

for name in favorite_numbers:
    if len(favorite_numbers[name]) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    for number in favorite_numbers[name]:
        print(f"\t{number}")
