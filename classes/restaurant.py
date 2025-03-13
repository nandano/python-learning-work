class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name.title()}.")
        print(f"Cuisine: {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")
    
    def set_number_served(self, customer_number):
        self.number_served = customer_number
    
    def increment_number_served(self, customer_number):
        self.number_served += customer_number
