# Simple Food - Digital (POS) System

A modular, Object-Oriented Programming (OOP) Point-of-Sale (POS) restaurant ordering application built with Python and Tkinter. This system features a graphical user interface (GUI), automatic stock validation, transaction calculation, real-time receipt generation, and data storage using JSON file handling.

---

## Project Structure

The project follows a modular architecture separating the user interface, business logic, object structures, and data handling components:

```
my_resturant_project/
│
├── Main.py               # Application entry point (Tkinter GUI, Screens, & Event Loops)
├── data.py               # Data Layer (JSON absolute path read/write management)
├── menu_item.py          # Class definitions for MenuItem (Base), Food, and Drink subclasses
├── resturant_order.py    # Transaction Manager (Cart logic, balance calculation, stock checks)
├── menu_data.json        # JSON database storing current item configurations and stock
└── README.md             # Project documentation (this file)
```

## Core Features

- Graphical User Interface: Built using Python's tkinter package with reactive entry widgets mapped to active database elements.

- Object-Oriented Design: Uses inheritance and encapsulation (MenuItem ➔ Food / Drink) to structure menu items cleanly.

- Input Validation: Safe try/except exception structures handle invalid non-numeric inputs (preventing ValueError crashes).

- Automated Stock Validation: Intercepts out-of-stock orders before checking out and notifies the user with screen alerts.

- Data Persistence: Automatically reads and writes state variations into menu_data.json using stable absolute paths to avoid terminal directory errors.

- Monospaced Receipt Generation: Dynamically generates a canvas receipt layout utilizing Courier typography for column-aligned financial printouts.


## Installation and Setup
Prerequisites
- Python 3.x installed on your local machine.

## Execution Instructions
- Clone the repository or navigate to your project directory:
```
cd path/to/my_resturant_project
```
- Run the main application file:
```
python Main.py
```
## Code Overview

- Object Models (menu_item.py)
Defines the structure of item elements. food and drink subclasses inherit core parameters (name, cost, quantity) from the parent menu_item class while tracking independent object generation counters.

- File Automation (data.py)
Provides atomic synchronization capabilities. Calculates absolute operational paths using the os path utilities to securely pull records from or back up to menu_data.json, parsing dictionaries back into fully instantiated active objects dynamically.

- Transaction Cart (resturant_order.py)
Maintains the individual customer checkout loop state. Controls stock subtraction limits and appends successful lines to total_item_list while incrementing the financial total_bill summary tracker.

- Application Desk (Main.py)
Clears and updates active frames inside the Tkinter application loop. Forwards frame reference instances safely via lambda callbacks to swap ordering windows with receipt canvases seamlessly.


## Testing Scenarios Implemented

- Successful Purchase: Quantities entered are deducted from the database, total bills are calculated, and tabular summary cards are drawn.

- Data Guarding: Typing text patterns (e.g., "abc") instead of whole numbers halts checkout loops via messagebox alerts.

- Inventory Bounds Protection: Requesting orders higher than available inventory numbers flags a warning and prevents transactions from modifying file states.


## Author and Academic Context

- Student Name: Kazeem Olalekan Sola-Raji

- Student ID: GH1053278

- Module: B100A Python Programming

- Institution: Gisma University of Applied Sciences
