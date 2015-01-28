import collections

FoodSource = collections.namedtuple(
    'FoodSource',
    'name, description')


barley = FoodSource('barley', 'a grain')
yams = FoodSource('yams', 'a tuber')
venison = FoodSource('venison', 'deer meat')
salmon = FoodSource('salmon', 'fish')
mutton = FoodSource('mutton', 'sheep meat')
peppers = FoodSource('peppers', 'green, yellow, and red')
rice = FoodSource('rice', 'a grain for wet areas')
apple = FoodSource('apple', 'a fruit')
blackberries = FoodSource('blackberries', 'berry bush')
