topping = ""

while topping != 'quit':
    topping = input("\nEnter the topping to add to your pizza:\n(Enter 'quit' to exit): ")
    if topping != 'quit':
        print(f"{topping} will be added to your pizza.")
