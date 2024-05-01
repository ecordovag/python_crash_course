# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

mom={"first_name":"Carmen","last_name":"Gonzales","age":"66","city":"Lima"}
sister={"first_name":"Angela","last_name":"Cordova","age":"33","city":"Barcelona"}
aunt={"first_name":"Delfi","last_name":"Díaz","age":"75","city":"Chosica"}

people=[mom,sister,aunt]

for relative in people:
    print(f"{relative["first_name"]} {relative["last_name"]}.")
    print(f"She is {relative["age"]} years old.")
    print(f"She lives in {relative["city"]}.\n")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places.

favorite_places={"Juan":["Lima","Chosica","Barranco"],
                 "Diego":["Viena","París"],
                 "Allison":["Washington"],
                 "Eleo":[],
                 }

for person,places in favorite_places.items():
    if len(places) >= 2:
        print(f"\n{person}'s favorite cities are:")
        for place in places:
            print(f"\t{place}")
    elif len(places) == 1:
        print(f"\n{person}'s favorite city is:")
        for place in places:
            print(f"\t{place}")
    else:
        print(f"\n{person} has no favorite cities!")