# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

prompt="\nEnter the pizza topping you'd like to add to your pizza"
prompt+="\nIf you have already entered all the pizza toppings you like, type quit "


while True:
    requested_topping=input(prompt)
    if requested_topping=="quit":
        break
    else:
        print(f"\nAdding {requested_topping} to your pizza!\n")


