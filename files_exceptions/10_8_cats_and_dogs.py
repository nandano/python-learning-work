from pathlib import Path

def read_names(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        names = contents.splitlines()
        print(f"\nNames in {path}: ")
        for name in names:
            print(name)

filenames = ['dogs.txt', 'cats.txt']
for file in filenames:
    path = Path(file)
    read_names(path)