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

user_1 = User("albert", 'einstein', 'germany')
user_2 = User('richard', 'feynman', 'usa')
user_3 = User('cv', 'raman', 'india')
user_4 = User('nikola', 'tesla', 'usa')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4.describe_user()
user_4.greet_user()