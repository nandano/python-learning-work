from pathlib import Path
import json

favorite_num = input("Enter your favorite number: ")
path = Path('favorite_number.txt')
contents = json.dumps(int(favorite_num))
path.write_text(contents)
