from random import choice

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
my_ticket = [3, 2, 7, 2]
winner_list = []
loops = 0

while my_ticket != winner_list:
    winner_list = []
    for digit in range(4):
        random_digit = choice(lottery_list)
        winner_list.append(random_digit)
    print(winner_list)
    loops += 1

print(f"No of times the loop had to run: {loops}")