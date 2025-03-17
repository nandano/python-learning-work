while True:
    num_1 = input("Enter a number: ")
    num_2 = input("Enter the second number: ")
    try:
        answer = int(num_1) + int(num_2)
    except ValueError:
        print("You can't add a number with a string 1D107")
    else:
        print(f"{num_1} + {num_2} = {answer}")
    
    more_nums = input("Do you want to add more numbers? (y/n): ")
    if more_nums == 'n':
        break