from pathlib import Path
import json

path = Path('user_dict.json')
user_dict = {}
username = input("Enter your username: ")
country = input("Enter your country: ")
favorite_number = input("Enter your favorite number: ")

user_dict['username'] = username
user_dict['country'] = country
user_dict['favorite_number'] = int(favorite_number)

contents = json.dumps(user_dict)
path.write_text(contents)

read_content = path.read_text()
read_dictionary = json.loads(read_content)
print(read_dictionary)