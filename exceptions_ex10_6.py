# 10-6. Addition: One common problem when prompting for numerical input occurs when people 
# provide text instead of numbers. When you try to convert the input to an int, you’ll get 
# a ValueError. Write a program that prompts for two numbers. Add them together and print 
# the result. Catch the ValueError if either input value is not a number, and print a 
# friendly error message. Test your program by entering two numbers and then by entering 
# some text instead of a number.

print("Please provide two integers and see the result of their addition")
print("Enter 'q' to quit")

first_number = input("Enter the first number ")
second_number = input("Enter the second number ")

try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("Those are not integers!")
else:
    print(f"The addition is {result}")