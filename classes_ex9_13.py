# 9-13. Dice: Make a class Dice with one attribute called sides, which has a default 
# value of 6. Write a method called roll_dice() that prints a random number between 1 
# and the number of sides the dice has. Make a 6-sided dice and roll it 10 times.
# Make a 10-sided dice and a 20-sided dice. Roll each dice 10 times.

from random import choice

class Dice:
    """ A class that describes a dices and rolls it """
    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_dice(self):
        numbers=[]
        for number in range(1,self.sides+1):
            numbers.append(number)
        chosen_num=choice(numbers)
        print(chosen_num)

# my_dice=Dice()
# my_dice.roll_dice()

# dice_2=Dice(10)
# dice_2.roll_dice()

dice_2=Dice(20)
dice_2.roll_dice()