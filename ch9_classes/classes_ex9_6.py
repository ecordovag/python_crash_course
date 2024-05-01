# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type
        self.number_served=0
            
    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.name}.")
        print(f"The type of cuisine this restaurant cooks is {self.cuisine}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self,num_cust=0):
        self.number_served=num_cust
        print(f"{self.name} has served {self.number_served} clients")

    def increment_number_served(self,clients_per_day):
        self.number_served += clients_per_day
        print(f"At the end of the day, {self.name} has served {self.number_served} clients.")
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=["chocolate","mint","coco"]
    
    def display_flavors(self):
        print(f"{self.name} has the following flavors available:")
        for flavor in self.flavors:  
            flavor=flavor.title()       
            print(f"\t- {flavor}")

ice_cream_1=IceCreamStand("Donofrio","Heladería")
ice_cream_1.display_flavors()
        