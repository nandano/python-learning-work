class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name.title()}.")
        print(f"Cuisine: {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

restaurant = Restaurant('tawa', 'chinese')
print(f"Name of restaurant: {restaurant.restaurant_name}.")
print(f"Type of cuisine is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()