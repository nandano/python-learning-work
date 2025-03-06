sandwich_orders = ['american sub', 'cemita', 'cuban', 'deli', 'naan']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nCompleted sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")