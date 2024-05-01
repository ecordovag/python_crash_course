# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store 
# two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
# that prints these two pieces of information, and a method called open_restaurant() that prints a 
# message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and 
# then call both methods.

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances 
#from the class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.cuisine=cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.name}.")
        print(f"The type of cuisine this restaurant cooks is {self.cuisine}.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant_1=Restaurant("La Posada", "comida criolla")
restaurant_2=Restaurant("Tenedores y palitos", "Chifa")
restaurant_3=Restaurant("Tinajas","Pollo a la brasa y parrillas")

print(f"The first restaurant is {restaurant_1.name}")
print(f"The type of food it cooks is {restaurant_1.cuisine}")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()