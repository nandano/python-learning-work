from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    favorite_num = json.loads(contents)
    print(f"I know your favorite number. It's {favorite_num}.")
else:
    favorite_num = input("Enter your favorite number: ")
    contents = json.dumps(int(favorite_num))
    path.write_text(contents)