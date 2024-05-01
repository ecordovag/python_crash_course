# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. 
# Randomly select 4 numbers or letters from the list and print a message saying that 
# any ticket matching these 4 numbers or letters wins a prize.

from random import choice

character_list=["a","b","c","d","e","1","2","3","4","5","6","7","8","9","10"]

my_ticket="dc16"
print(f"Your ticket is {my_ticket}")

elected_characters=0
winning_ticket=""

while elected_characters < 4:
    elected_character=choice(character_list)
    print(f"The character elected is {elected_character}.")
    character_list.remove(elected_character)
    winning_ticket += elected_character
    elected_characters += 1

print(f"The winning ticket is {str(winning_ticket)}")

count=0
for character in winning_ticket:
    if character not in my_ticket:
        print("You didn't win!")
        break
    count += 1
    if count == 4:
        print("You win!")
    
    