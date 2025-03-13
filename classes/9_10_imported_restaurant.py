from restaurant import Restaurant

restaurant_1 = Restaurant('sai', 'chinese')
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(150)
print(restaurant_1.number_served)
restaurant_1.increment_number_served(12)
print(restaurant_1.number_served)