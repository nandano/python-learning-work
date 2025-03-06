# uses conditional test in while statement
# topping = ""

# while topping != 'quit':
#     topping = input("\nEnter the topping to add to your pizza:\n(Enter 'quit' to exit): ")
#     if topping != 'quit':
#         print(f"{topping} will be added to your pizza.")

# uses an active variable
# active = True

# while active:
#     topping = input("\nEnter the topping you want in your pizza.\n(Enter 'quit' to exit): ")
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"{topping} will be added to your pizza.")

# uses break statement to exit the loop
while True:
    topping = input("\nEnter the topping you want in your pizza.\n(Enter 'quit' to exit): ")
    if topping == 'quit':
        break
    print(f"{topping} will be added to your pizza.")
