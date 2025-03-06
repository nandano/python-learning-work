age = 0

while True:
    age = input("Enter your age: ")
    age = int(age)

    if age < 3:
        print("Your ticket is FREE.")
    elif age <= 12:
        print("Please pay $10.")
    else:
        print("Please pay $15.")
