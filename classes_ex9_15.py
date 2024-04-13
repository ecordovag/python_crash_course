# # 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the 
# kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a 
# loop that keeps pulling numbers until your ticket wins. Print a message reporting 
# how many times the loop had to run to give you a winning ticket.

from random import choice

character_list=["a","b","c","d","e","1","2","3","4","5","6","7","8","9","10"]

my_ticket="dc16"
print(f"Your ticket is {my_ticket}")

remaining_similities=4
active=True
loop_number=0
while active:
    elected_character=choice(character_list)
    print(f"The character elected is {elected_character}.")
    character_list.remove(elected_character)
    loop_number += 1
    if elected_character in my_ticket:
        remaining_similities -= 1
    else:
        continue
    if remaining_similities == 0:
        print(f"The loop had to run {loop_number} times until you won.")
        active=False
       
            


