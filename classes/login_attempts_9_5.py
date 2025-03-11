class User:
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nFull name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Country of residence: {self.country.title()}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!".title())
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('albert', 'einstein', 'germany')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}.")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}.")