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
    count = 0
    # filter_cars = {'slow_cars': slow_cars, 'fast_cars': fast_cars, 'sport_cars': sport_cars, 'cheap': cheap, 'medium': medium, 'expensive': expensive}
    filter_cars = defaultdict(list)


    def __init__(self, car_object):
        self.car_object = car_object
        Cars.count += 1
        self.car_object['id'] = Cars.count

    def get_brand(self):
        Cars.brands[self.car_object['brand']].append(self.car_object)

    def get_hp(self):
        horse_power = int(self.car_object['hp'])
        if horse_power < 120:
            Cars.filter_cars['slow_cars'].append(self.car_object)
        elif 120 <= horse_power < 180:
            Cars.filter_cars['fast_cars'].append(self.car_object)
        elif horse_power >= 180:
            Cars.filter_cars['sport_cars'].append(self.car_object)

    def get_price(self):
        price = int(self.car_object['price'])
        if price < 1000:
            Cars.filter_cars['cheap'].append(self.car_object)
        elif 1000 <= price < 5000:
            Cars.filter_cars['medium'].append(self.car_object)
        elif price >= 5000:
            Cars.filter_cars['expensive'].append(self.car_object)

    def evaluate_cars(self):
        self.get_hp()
        self.get_price()
        self.get_brand()
