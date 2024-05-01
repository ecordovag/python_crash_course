# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

# car=input("What kind of rental car do you want? ")
# print(f"Let me see if I can find you a {car}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

# comensales=input("¿Cuántas personas hay en el grupo? ")
# comensales=int(comensales)
# if comensales > 8:
#     print("Tendrán que esperar a que se desocupe una mesa.")
# else:
#     print("La mesa está lista.")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)