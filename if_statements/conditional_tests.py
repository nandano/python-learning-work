car = 'suzuki'
print("Is car == 'suzuki'? I predict True")
print(car == 'suzuki')

print("\nIs car == 'skoda'? I predict False")
print(car == 'skoda')

print("\nIs car == 'honda'? I predict False")
print(car == 'honda')

subject = 'mathematics'
print("\nIs subject == 'physics'? I predict False")
print(subject == 'physics')

print("\nIs subject == 'math'? I predict False")
print(subject == 'math')

print("\nIs subject == 'mathematics'? I predict True")
print(subject == 'mathematics')

subject = 'Maths'
print("\nIs subject == 'maths'? I predict False")
print(subject == 'maths')

print("\nIs subject.lower() == 'maths' I predict True")
print(subject.lower() == 'maths')

print("\nIs 5 > 2? I predict True")
print(5 > 2)

print("\nIs 10 < 1? I predict False")
print(10 < 1)

print("\nIs 5 >= 5? I predict True")
print(5 >= 5)

print("\nIs 10 <= 10? I predict True")
print(10 <= 10)

print("\nI predict False")
print(5 > 10 and 10 == 10)

print("\nI predict True")
print(5 == 10 or subject == 'Maths')

subjects = ['maths', 'physics', 'computer science', 'english']
print("\nIs 'physics' in subjects? I predict True")
print('physics' in subjects)

print("\nIs 'Physics' in subjects? I predict False")
print("Physics" in subjects)

print("\nIs 'mathematics' not in subjects? I predict True")
print("mathematics" not in subjects)

print("\nIs 'physics' not in subjects? I predict False")
print('physics' not in subjects)