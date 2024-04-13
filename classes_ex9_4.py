# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers 
# the restaurant has served, and then change this value and print it again.

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

    def counting_clients(self):
        print(f"{self.name} has served {self.number_served} clients") 

restaurant1=Restaurant("Restaurant","criolla")
restaurant1.counting_clients()
restaurant1.number_served=5
restaurant1.counting_clients()