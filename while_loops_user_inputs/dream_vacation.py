dream_destinations = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    dream_destinations[name] = destination

    should_continue = input("Do you want to let another person take the poll? (yes / no): ")
    if should_continue == 'no':
        poll_active = False

print("\nPoll Results:")
for name, destination in dream_destinations.items():
    print(f"{name.title()} would like to visit {destination.title()} someday.")
