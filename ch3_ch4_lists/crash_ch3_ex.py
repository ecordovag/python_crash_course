 # 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

# invited=["Angela","Carmen","Delfi"]
# for i in invited:
#     print(f"¡Hola, {i}! ¿quisieras venir a cenar a mi casa?")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

# invited=["Angela","Carmen","Delfi"]
# for i in invited:
#     print(f"¡Hola, {i}! ¿quisieras venir a cenar a mi casa?")
# print(f"\nMe acaban de decir que {invited[2]} no puede venir a la reunión.\n")
# invited[2]="Pedro"
# for i in invited:
#     print(f"¡Hola, {i}! ¿quisieras venir a cenar a mi casa?")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
    
# invited=["Angela","Carmen","Delfi"]
# for i in invited:
#     print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")
# print(f"\nMe acaban de decir que {invited[2]} no puede venir a la reunión.\n")
# invited[2]="Pedro"
# for i in invited:
#     print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")
# print("\n¡He encontrado una mesa más grande para cenar!\n")
# invited.insert(0,"María")
# invited.insert(2,"Jesus")
# invited.append("Victoria")
# for i in invited:
#     print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

invited=["Angela","Carmen","Delfi"]
for i in invited:
    print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")
print(f"\nMe acaban de decir que {invited[2]} no puede venir a la reunión.\n")
invited[2]="Pedro"
for i in invited:
    print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")
print("\n¡He encontrado una mesa más grande para cenar!\n")
invited.insert(0,"María")
invited.insert(2,"Jesus")
invited.append("Victoria")
for i in invited:
    print(f"¡Hola, {i}!, ¿quisieras venir a cenar a mi casa?")
print("\nLamentablemente, la nueva mesa no va a llegar y solo puedo invitar a dos personas.\n")
while len(invited)>2:
    rem_guest=invited.pop(-1)
    print(f"Lo siento, {rem_guest}, no puedo invitarte a cenar.")
print("\n")
for i in invited:
    print(f"¡Hola, {i}!, ¡todavía estás invitado!")
del invited[0]
del invited[0]
print("\n")
print(invited)