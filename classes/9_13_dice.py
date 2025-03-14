from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

my_die = Die()
print("\n6 sided die:")
for turn in range(10):
    my_die.roll_die()

ten_die = Die(10)
print("\n10 sided die:")

for turn in range(10):
    ten_die.roll_die()

print("\n20 sided die:")
twenty_die = Die(20)
for turn in range(10):
    twenty_die.roll_die()