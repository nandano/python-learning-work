from pathlib import Path

path = Path('guest_book.txt')
contents = ''
while True:
    name = input("Enter your name: ")
    contents += name + '\n'

    more_names = input("Do you want to enter more names?(y/n): ")
    if more_names == 'n':
        break

path.write_text(contents)