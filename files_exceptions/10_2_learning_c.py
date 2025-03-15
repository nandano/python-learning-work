from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

c_contents = contents.replace('Python', 'C')
for line in c_contents.splitlines():
    print(line)