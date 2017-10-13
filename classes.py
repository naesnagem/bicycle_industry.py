class Bicycle(object):
    def __init__(self, model, weight, production_cost, units):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost
        self.units = units


class Bike_Store(object):
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    def in_budget(self, customer, margin = 1.2):
        options = []
        for bike in self.inventory:
            if self.inventory[bike].production_cost * margin <= customers[customer].wallet:
                options.append(self.inventory[bike].model)
            print("{1} can afford to buy: {2}".format(customers[customer].name, options))
        return options
    
    def sell(self, wallet, margin = 1.2):
        self.wallet = wallet
        choice = ()


class Customers(object):
    def __init__(self, name, wallet ):
        self.name = name
        self.wallet = wallet
        self.margin = 1.2
        