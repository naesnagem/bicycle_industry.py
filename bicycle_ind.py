import random
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


    showroom = [bike_1, bike_2, bike_3, bike_4, bike_5, bike_6 ]
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
    for customer in range(len(customers)):
        print("{} can afford these bikes:".format(customers[customer].name))
        options = []
        for bike in range(len(showroom)):
            if showroom[bike].production_cost * 1.2 <= customers[customer].wallet:
                options.append(store.inventory[bike].model)
        print(options)
    
    
    """
    Print the initial inventory of the bike shop for each bike it carries.
    """
    
    print("\n{} has an initial inventory of these bikes:".format(store.name))
    for bike in range(len(showroom)):
        print(showroom[bike].model)
    
    """    
    Have each of the three customers purchase a bike then print the name of the bike the customer 
    purchased, the cost, and how much money they have left over in their bicycle fund.
    """
    for customer in range(len(customers)):
        print("\n{} has decided to buy:".format(customers[customer].name))
        print(random.choice(options))