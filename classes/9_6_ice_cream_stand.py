class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name.title()}.")
        print(f"Cuisine: {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("The available flavors are:")
        for flavor in self.flavors:
            print(f"\t-{flavor}")

stand = IceCreamStand('golden experience', 'ice cream', ['strawberry', 'butterscotch', 'pista', 'vanilla', 'chocolate'])
stand.describe_restaurant()
stand.open_restaurant()
stand.display_flavors()