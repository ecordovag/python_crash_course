# Continue statement. Ch.7
print("With continue statement")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("\nWithout continue statement")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        print(current_number)