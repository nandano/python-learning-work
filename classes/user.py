class User:
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
    
    def describe_user(self):
        print(f"\nFull name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Country of residence: {self.country.title()}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!".title())
