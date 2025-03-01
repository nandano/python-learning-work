usernames = ['admin', 'rajesh', 'naren', 'jack', 'rose']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see the status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
