class Bicycle(object):
    def __init__(self, model, weight, production_cost, units):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost
        self.units = units
    
class Customers(object):
    def __init__(self, name, wallet ):
        self.name = name
        self.wallet = wallet
    

class Bike_Store(object):
    def __init__(self, name, margin = 1.2, inventory = {}, budget = {}, profit = 0):
        self.name = name
        self.margin = margin
        self.inventory = inventory
        self.budget = budget
        self.profit = profit
    


