from pathlib import Path
import json

path = Path('favorite_number.txt')
contents = path.read_text()
favorite_num = json.loads(contents)
print(f"I know your favorite number! It's {favorite_num}.")
