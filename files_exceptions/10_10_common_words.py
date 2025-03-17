from pathlib import Path

def the_counter(path):
    try:
        contents = path.read_text(encoding='utf-8').lower()
    except FileNotFoundError:
        print(f"{path} does not exist.")
    else:
        count = contents.count('the')
        print(f"'the' occurs {count} times in {path}")

filenames = ['romeo_juliet.txt', 'frankenstein.txt']
for filename in filenames:
    path = Path(filename)
    the_counter(path)