# PennyWise

Overview

This project involves creating a menu-based expense tracker application that allows users to add participants, record expenses, display participant information, show expense summaries, and export data to a CSV file. The application is designed to manage expenses shared among multiple participants and keep track of who owes or gets back money.
Features and Requirements
Menu Options

    Add Participant(s):
        Add one or more unique names of participants who will be involved in the transactions.
    Add Expense:
        Record an expense by specifying who paid, the amount paid, and how the expense is distributed among participants.
    Show All Participants:
        Display the names of all participants currently added.
    Show Expenses:
        Display a summary table showing each participant’s expenses and how much they owe or get back.
    Exit/Export:
        Export all data to a CSV file named expenses.csv and exit the program.

Input/Output

    Input: User inputs via the console.
    Output: Display information on the console and export data to a CSV file.

Implementation Details
Prerequisites

    Python 3.x: Required to run the program.

Setup and Installation

    Clone the Repository:

    sh

git clone <repository-url>
cd expense-tracker

Run the Application:

    Execute the Python script expense_tracker.py in your terminal:

    sh

        python expense_tracker.py

Code Explanation
Data Structure

    Participants Dictionary:
        Key: Participant's name (string)
        Value: Net amount (float) indicating how much they owe or get back.

Functions

    add_participants():
        Clear existing participants and add new participants to the dictionary.
        Input: Number of participants and their names.
        Output: Confirmation message.

    add_expense():
        Record an expense by taking the payer's name, amount paid, and names of participants involved.
        Calculate the share of each participant and update the dictionary.
        Output: Confirmation message.

    show_participants():
        Display the names of all participants.
        Output: List of participant names.

    show_expenses():
        Display a table summarizing each participant’s net amount.
        Output: Table with participant names and their net amount.

    write_to_csv():
        Export participant data to a CSV file named expenses.csv.
        Output: Confirmation message and CSV file.

Usage
Menu Navigation

    Add Participant(s):
        Select option 1 and follow the prompts to add participants.
    Add Expense:
        Select option 2 and follow the prompts to record an expense.
    Show All Participants:
        Select option 3 to display all participant names.
    Show Expenses:
        Select option 4 to display the expense summary table.
    Exit/Export:
        Select option 5 to export data to expenses.csv and exit the program.
