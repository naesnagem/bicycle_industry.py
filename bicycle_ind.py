import random
import math
from classes import Bicycle, Bike_Store, Customers

if __name__ == '__main__':

    """
    Create a bicycle shop that has 6 different bicycle models in stock. 
    The shop should charge its customers 20% over the cost of the bikes.
    """
    
    bike_1 =Bicycle("Road Warrior", 5, 150, 30)
    bike_2 =Bicycle("Downhill Racer", 7, 250, 35)
    bike_3 =Bicycle("Steel Horse", 10, 375, 20)
    bike_4 =Bicycle("Magic Carpet", 12, 650, 20)
    bike_5 =Bicycle("Speedy Gonzalez", 8, 800, 15)
    bike_6 =Bicycle("Bugs Bunny", 4, 125, 15)

    showroom = [Bicycle("Road Warrior", 5, 150, 30), Bicycle("Downhill Racer", 7, 250, 35), Bicycle("Steel Horse", 10, 375, 20), 
    Bicycle("Magic Carpet", 12, 650, 20), Bicycle("Speedy Gonzalez", 8, 800, 15), Bicycle("Bugs Bunny", 4, 125, 15)]
    store = Bike_Store("Good Bikes", showroom)
    
    """
    Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
    """

    customer_1 = Customers("Kevin", 200)
    customer_2 = Customers("Paul", 500)
    customer_3 = Customers("Jen", 1000)

    customers = [customer_1, customer_2, customer_3]
    
    
    """
    Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
    Make sure you price the bikes in such a way that each customer can afford at least one.
    """
    for customer in customers:
        print("{} can afford these bikes:".format(customer.name))
        options = []
        for bike in showroom:
            if bike.production_cost*1.2 <= customer.wallet:
                options.append(bike.model)
        print(options)
    
    """
    Print the initial inventory of the bike shop for each bike it carries.
    """
    
    print("\n{} has an initial inventory of these bikes:".format(store.name))
    for bike in showroom:
        print(bike.units, "units of the", bike.model, "model")
    
    """    
    Have each of the three customers purchase a bike then print the name of the bike the customer 
    purchased, the cost, and how much money they have left over in their bicycle fund.
    """
    for customer in customers:
        print("\nAfter considering the different options {} has decided to buy:".format(customer.name))
        a = []
        for bike in showroom:
            if bike.production_cost * 1.2 <= customer.wallet:
                a.append(bike)
            b = random.choice(a)
        print("The", b.model, "model which has a price of: {}".format(b.production_cost*1.2))
        print("This leaves {} with:".format(customer.name))
        print(customer.wallet - (b.production_cost*1.2), "after purchasing the bike")
        print("This sale created a profit of {} for the bikeshop".format(b.production_cost*.2))
        for bike in showroom:
            if b.model == bike.model:
                bike.units -= 1

    """    
    After each customer has purchased their bike, the script should print out the bicycle shop's 
    remaining inventory for each bike, and how much profit they have made selling the three bikes.
    """ 
    print("\nHere is the updated inventory:")
    for bike in showroom:
        print(bike.model, bike.units)
        
    print("\nThe total profit generated from these sales is")
