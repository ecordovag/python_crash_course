# 10-14. Verify User: The final listing for remember_me.py assumes either that the user has 
# already entered their username or that the program is running for the first time. We should 
# modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if this is the correct 
# username. If it’s not, call get_new_username() to get the correct username.


from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for a new username."""
    user_info = {}
    username = input("What is your name? ")
    user_info["username"] = username
    age = input("How old are you? ")
    user_info["age"] = age
    place = input("Where do you live? ")
    user_info["place"] = place
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print("Please, answer 'yes' or 'no' to the following question:")
        answer = input(f"Is this your username? {user_info["username"]} ")
        if answer == "yes":
            print(f"Welcome back, {user_info["username"]}! Here's your data:")
            print(f"\tName: {user_info["username"]}")
            print(f"\tAge: {user_info["age"]}")
            print(f"\tYou live in: {user_info["place"]}")
        else:
            user_info = get_new_user_info(path)
            print(f"We'll remember you when you come back, {user_info["username"]}!") 
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info["username"]}!")

greet_user()