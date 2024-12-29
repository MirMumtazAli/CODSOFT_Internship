# QuickCalc

This is a simple command-line calculator application built with Python. The program prompts the user to input two numbers and choose an arithmetic operation (addition, subtraction, multiplication, or division). It then performs the operation and displays the result.

## Features

- Accepts two integer inputs from the user.
- Supports the following arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Handles invalid inputs and displays error messages.

## Requirements

- Python 3.x or higher


## Usage

1. Run the script:
   ```bash
   python calculator.py
   ```
2. Follow the on-screen instructions:
   - Enter two numbers when prompted.
   - Select an arithmetic operation from the provided menu.
   - The result will be displayed on the screen.

## Example Output

```
Welcome to the Calculator!
------------------------------
Enter First Number: 10
Enter Second Number: 5
------------------------------
Arithmetic Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter the Operation number from above : 1
------------------------------
The Addition of 10 and 5 is 15
```

## Error Handling

- If invalid inputs are entered (non-numeric), the program will prompt the user to enter valid numbers.
- If an invalid operation number is selected, the program will request a valid input.
- Division by zero is handled gracefully with an error message.
