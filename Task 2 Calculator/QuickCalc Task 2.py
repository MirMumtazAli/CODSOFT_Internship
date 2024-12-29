# ------CALCULATOR------
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

print('Welcome to the Calculator!')
print(30 * "-")

while True:
    try:
        First_number = int(input('Enter First Number: '))
        Second_number = int(input('Enter Second Number: '))
        print(30 * '-')
        break  # Exit the loop if the inputs are valid integers
    except ValueError:
        print('Please enter valid input numbers.')
        print(30 * '-')


# Repeat until a valid operation is entered
while True:
    try:
        print(''' Arithmetic Operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    ''')
        Operations = int(input('Enter the Operation number from above : '))
        print(30 * '-')
        if Operations in range(1,5): # Check if the operation is valid
            break # Exit the loop if valid
    except ValueError:
        print(30 * '-')
        print('Invalid operation number.')
        print(30 * '-')
        
        
# Performing the calculation
if Operations == 1:
    print(f'The Addition of {First_number} and {Second_number} is {First_number + Second_number}')
elif Operations == 2:
    print(f'The Subtraction of {First_number} and {Second_number} is {First_number - Second_number}')
elif Operations == 3:
    print(f'The Multiplication of {First_number} and {Second_number} is {First_number * Second_number}')
else :
    try:
        print(f'The Division of {First_number} and {Second_number} is {First_number / Second_number}')
    except ZeroDivisionError: # Raises ZeroDivisionError
        print('Division by zero is not defined.')
