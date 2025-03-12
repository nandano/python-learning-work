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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin's privileges are:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, country, privileges):
        super().__init__(first_name, last_name, country)
        self.privileges = Privileges(privileges)


admin = Admin('joseph', 'joestar', 'america', ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()