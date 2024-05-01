# 10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop 
# so the user can continue entering numbers, even if they make a mistake and 
# enter text instead of a number.

while True:
    print("Please provide two integers and see the result of their addition")
    print("Enter 'q' to quit")

    first_number = input("Enter the first number ")
    if first_number == "q":
        break
    second_number = input("Enter the second number ")  
    if second_number == "q":
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Those are not integers!")
    else:
        print(f"The addition is {result}")