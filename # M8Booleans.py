# Lela Parks
# Nov 12, 2024

# This program compares two user inputs and prints whether they are equal or not.

def compare_inputs():
    # Take two inputs from the user
    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")
    
    # Compare and print if they are equal or not
    if input1 == input2:
        print("The values are equal.")
    else:
        print("The values are not equal.")
def sum_comparison():
    # Take two inputs from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Compare the sum with 10 and print the appropriate message
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")
def check_value_in_list():
    # Take a list input from the user
    lst = input("Enter a list of numbers (separate them by spaces): ").split()
    
    # Convert each element to integer
    lst = [int(i) for i in lst]
    
    # Check if 5 is in the list and print the result
    if 5 in lst:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")
def is_leap_year(year):
    # Check the leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Save this code in resources.py

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses


# Creating the first character
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

# Adding your own character
player2 = Character('Lela-Parks', ['rope', 'pen', 'paper', 'idea'], ['small', 'confusion'])
for item in player2.weapons:
    print("Item: ", item)
for debuff in player2.weaknesses:
    print("Debuff: ", debuff)
# Save this code in M7Booleans.py

def task_check(task_number):
    # Game character items and weaknesses
    items = ['pan', 'paper', 'idea', 'rope', 'groceries']
    weaknesses = ['slow']

    if task_number == 1:  # Task 1: Climb a mountain
        required_items = ['rope', 'coat', 'first aid kit']
        if all(item in items for item in required_items) and 'slow' not in weaknesses:
            print("Task 1 (Climb a mountain) is possible.")
        else:
            print("Task 1 (Climb a mountain) is not possible.")

    elif task_number == 2:  # Task 2: Cook a meal
        required_items = ['pan', 'groceries']
        if all(item in items for item in required_items) and 'small' not in weaknesses:
            print("Task 2 (Cook a meal) is possible.")
        else:
            print("Task 2 (Cook a meal) is not possible.")

    elif task_number == 3:  # Task 3: Write a book
        required_items = ['pen', 'paper', 'idea']
        if all(item in items for item in required_items) and 'confusion' not in weaknesses:
            print("Task 3 (Write a book) is possible.")
        else:
            print("Task 3 (Write a book) is not possible.")

    else:
        print("Invalid task number. Please enter 1, 2, or 3.")

# Test the function
task_check(1)  # Check task 1
task_check(2)  # Check task 2
task_check(3)  # Check task 3

