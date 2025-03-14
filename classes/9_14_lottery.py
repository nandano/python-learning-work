from random import choice

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
winner = ''

for digit in range(4):
    random_number = choice(lottery_list)
    winner += str(random_number)

print(f"Winner ticket: {winner}")