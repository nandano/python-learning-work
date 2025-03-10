class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name of restaurant: {self.restaurant_name.title()}.")
        print(f"Cuisine: {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

restaurant_1 = Restaurant('italian delight', 'italian')
restaurant_2 = Restaurant('royal cafe', 'indian')
restaurant_3 = Restaurant('kannadi', 'kerala')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()