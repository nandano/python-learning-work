from user import User

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
