current_users = ['admin', 'Rajesh', 'naren', 'jack', 'rose']
current_users_lower = [user.lower() for user in current_users]
new_users = ['RAJESH', 'rose', 'marvin', 'erwin', 'isaac']

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username {user} already exists. Please enter a new username.")
    else:
        print(f"The username {user} is available.")
