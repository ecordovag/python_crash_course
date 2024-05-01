# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.

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
    
 
restaurant1=Restaurant("Restaurant","criolla")
restaurant1.set_number_served()
restaurant1.set_number_served(5)