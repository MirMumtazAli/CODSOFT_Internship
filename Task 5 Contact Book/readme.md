# EasyConnect Address Book

The **Contact Book Application** is a simple yet effective tool designed to manage personal or professional contact information. With its intuitive interface built using Python's Tkinter library, it enables users to store, search, update, and delete contacts seamlessly.  

---

## Table of Contents  
- [Features](#features)  
- [How It Works](#how-it-works)  
- [Requirements](#requirements)  
- [Setup and Usage](#setup-and-usage)  
- [Code Highlights](#code-highlights)
- [Screenshots](#screenshots)  
- [Future Enhancements](#future-enhancements)  
- [License](#license)  

---

## Features  

1. **Add New Contacts**  
   - Save names, phone numbers, email addresses, and home addresses.  
   - Ensures phone number uniqueness to prevent duplicate entries.  

2. **Search Contacts**  
   - Quickly find contacts using a search bar with instant feedback.  

3. **Update Existing Contacts**  
   - Modify details such as name, phone number, email, or address.  

4. **Delete Contacts**  
   - Remove unwanted or outdated contact entries by name or phone number.  

5. **User-Friendly Interface**  
   - A clean and interactive design with separate sections for saving, searching, updating, and deleting contacts.  

---

## How It Works  

### Contact Management  
- **Saving Contacts**: Users provide required information, and the app validates and stores it in a dynamic list.  
- **Searching Contacts**: The app searches for matches in the contact list and highlights results in the displayed list.  
- **Updating Contacts**: Users can search for a contact, edit its details, and save changes.  
- **Deleting Contacts**: Contacts can be removed by name or phone number.  

### User Interface  
The app uses a Tkinter-based GUI with frames for different operations. A centralized listbox displays all saved contacts in a formatted table style.  

---

## Requirements  

- **Python 3.7 or later**  
- **Tkinter** (bundled with most Python installations)  

---

## Setup and Usage  

### Installation  

1. Clone this repository or download the source code as a ZIP file.  
2. Extract the files and navigate to the project directory.  

### Running the Application  

1. Open a terminal or command prompt in the project directory.  
2. Run the script:  
   ```bash  
   python Task 5 EasyConnect Address Book.py  
   ```  
3. The Contact Book application will open in a new window.  

---

## Code Highlights  

### Contact List Storage  
Contacts are stored as lists in the following format:  
```python  
contacts = [  
    ["Name", "Phone Number", "Email ID", "Address"]  
]  
```  

### Key Functions  
- `search_contact`: Handles search queries and displays matching results in the contact list.  
- `new_contact_insertion`: Validates inputs and saves new contacts.  
- `del_contact`: Deletes contacts based on input criteria.  
- `apply_update`: Updates contact details and refreshes the contact list display.  

---

## Screenshot
<img width="960" alt="output" src="https://github.com/user-attachments/assets/7abb22e7-351c-4d03-a344-37c0579cfbdf" />

---

## Future Enhancements  

- **Persistent Storage**: Save contacts to a file (CSV/JSON) or database for long-term use.  
- **Advanced Search**: Allow partial matches and support for multiple search criteria.  
- **UI Improvements**: Add themes and more responsive designs for better usability.  
- **Error Handling**: Handle edge cases and unexpected inputs more robustly.  
- **Export/Import Functionality**: Enable users to export their contact list and import it into another system.  

---

## License  

This project is open-source and available under the MIT License.  
