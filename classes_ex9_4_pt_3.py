# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

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

restaurant1=Restaurant("Restaurant","criolla")
restaurant1.set_number_served()
restaurant1.increment_number_served(15)
restaurant1.set_number_served(1)
restaurant1.increment_number_served(15)