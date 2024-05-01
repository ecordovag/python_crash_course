# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test file for Employee with two test functions, test_give_default
# _raise() and test_give_custom_raise(). Write your tests once without using a
# fixture, and make sure they both pass. Then write a fixture so you don’t have to
# create a new employee instance in each test function. Run the tests again, and
# make sure both tests still pass.

class Employee:
    """ An attempt to represent an employee"""

    def __init__(self, first, last, salary):
        """Initialize the attibutes to describe an employee"""
        self.first_name = first
        self. last_name = last
        self.salary = salary
    
    def give_raise(self,increment=5000):
        new_salary = self.salary + increment
        return new_salary
