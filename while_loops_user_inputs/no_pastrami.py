sandwich_orders = ['pastrami', 'american sub', 'cemita', 'pastrami', 'cuban', 'deli', 'pastrami', 'naan']
finished_sandwiches = []

print("The Deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")