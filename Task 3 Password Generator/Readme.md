# Task 3 PassGen Pro

A Python-based desktop application for generating secure passwords. The application uses the Tkinter library to provide a graphical user interface (GUI) that allows users to customize password length and character types.

## Features

- **User-Friendly Interface**: A clean and intuitive GUI built with Tkinter.
- **Customizable Passwords**:
  - Specify password length.
  - Choose from uppercase letters, lowercase letters, numeric digits, and symbols.
- **Password Complexity Indicator**: Provides feedback on the strength of the password based on selected character types.
- **Clipboard Support**: Easily copy the generated password to your clipboard.


## Usage

1. Run the application:
   ```bash
   python Task 3 PassGen Pro.py
   ```

2. In the application window:
   - Enter the desired password length.
   - Select the character types to include (uppercase, lowercase, digits, symbols).
   - Click `GENERATE!` to create a password.
   - Optionally, click `Copy Password` to copy the generated password to your clipboard.

## Code Highlights

- **Password Length and Validation**:
  Ensures a valid length is provided before generating passwords.

- **Character Type Selection**:
  Includes checkboxes to choose character types, enhancing password security.

- **Password Complexity Feedback**:
  - `Very Weak`: Only one character type selected.
  - `Weak`: Two character types selected.
  - `Strong`: Three character types selected.
  - `Very Strong`: All character types selected.

- **Clipboard Integration**:
  Simplifies saving passwords by allowing direct copying to the system clipboard.


# 👁️ Visual Preview:
![Task 3 password generator output](https://github.com/user-attachments/assets/d1c6cbaa-72f0-4c6f-8d60-1673e7aec9a4)


## File Overview

- `Task 3 PassGen Pro.py`: Main application script.

## Contributing

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
