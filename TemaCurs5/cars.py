import copy
from collections import defaultdict


class Cars:

    slow_cars = []
    fast_cars = []
    sport_cars = []
    cheap = []
    medium = []
    expensive = []
    brands = defaultdict(list)

    filter_cars = {'slow_cars':slow_cars, 'fast_cars':fast_cars, 'sport_cars':sport_cars, 'cheap':cheap, 'medium':medium, 'expensive':expensive}

    def __init__(self, car_object):
        self.car_object = car_object

    def get_brand(self):
        Cars.brands[self.car_object['brand']].append(self.car_object)

    def get_hp(self):
        horse_power = int(self.car_object['hp'])
        if horse_power<120:
            Cars.slow_cars.append(self.car_object)
        elif 120 <= horse_power < 180:
            Cars.fast_cars.append(self.car_object)
        elif horse_power>=180:
            Cars.sport_cars.append(self.car_object)

    def get_price(self):
        price = int(self.car_object['price'])
        if price <1000:
            Cars.cheap.append(self.car_object)
        elif price >=1000 and price <5000:
            Cars.medium.append(self.car_object)
        elif price >=5000:
            Cars.expensive.append(self.car_object)

    def evaluate_cars(self):
        self.get_hp()
        self.get_price()
        self.get_brand()








