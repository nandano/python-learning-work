def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model

    return car_info

car = make_car('tata', 'harrier', color='black', at=True)
print(car)