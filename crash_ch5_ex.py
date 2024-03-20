# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
# and write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned 5
# points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# Write one version of this program that runs the if block and another that
# runs the else block

# color="green"
# if color=="green":
#     gained=5
#     print("You shot the alien!")
# else:
#     gained=10
# print(f"You earn {gained} points!")

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# # chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

color="red"
if color=="green":
    gained=5
elif color=="yellow":
    gained=10
elif color=="red":
    gained=15
print(f"You earn {gained} points!")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user.
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message
# is printed.

users_list=[]
if users_list:
    for user in users_list:
        if user=="admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello, {user},thank you for logging in again.")
else:
    print("We need to find some users!")