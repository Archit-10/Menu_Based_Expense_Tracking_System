Welcome to PennyWise, your straightforward, Python-powered solution for tracking group expenses. Whether you're managing a weekend getaway, a project expense report, or a casual meal with friends, PennyWise helps you keep finances clear and fair. Built with a minimal, menu-driven interface, it’s perfect for those who want a quick, transparent way to split expenses.
📌 Features

    Add Participants
    Effortlessly add multiple participants by name, each initializing with a balance of zero. This sets the groundwork for tracking each individual’s share of group expenses.

    Log Expenses
    Record expenses by specifying:
        The payer
        The total amount
        Participants involved in that expense

    PennyWise then calculates each participant's share automatically, allocating costs accurately based on the input.

    View Participants
    List all participants to keep track of who's involved in the current session.

    Show Balance
    See who owes what or gets back money. PennyWise calculates each participant's balance relative to the average contribution, showing a clear picture of who needs to settle up.

    Export to CSV
    With a single click, export the expense data to expenses.csv for easy sharing and record-keeping.

📋 Installation and Usage

    Clone the Repository:

    bash

git clone <repo-url>
cd pennywise

Run the Program:

bash

    python expense_tracker.py

    Follow the Menu Options:
    The menu will prompt you through adding participants, logging expenses, viewing balances, and exporting data to a CSV file when you’re done.

💡 Sample Walkthrough

    Add participants with their names.
    Record an expense, indicating who paid and how much, along with the participants sharing the cost.
    View individual balances to see who owes or gets back money.
    Export your expense data in a neat CSV format before exiting the program.

Example Usage

Here's a quick example of how a session might look:

plaintext

Menu:
1. Add participant(s)
2. Add expense
3. Show all participants
4. Show expenses
5. Exit/Export

Select an option: 1
Enter the number of participants: 3
Enter participant's name: Alice
Enter participant's name: Bob
Enter participant's name: Carol

Select an option: 2
Paid by: Alice
Amount: 60
Distributed amongst (comma separated): Alice, Bob, Carol

Expense added successfully.

Select an option: 4
Expenses:
Participant's Name           Amount Owes/Gets Back  
Alice                         +20.0
Bob                           -10.0
Carol                         -10.0

📝 Data Export

After completing all entries, export your data to a CSV file (expenses.csv). The file includes each participant's net balance, making it easy to share or review your finances.
📎 Suggested Images

For an added professional touch, include an image of a sample CSV output and a screenshot of the terminal running the program to give a clear preview of the tool’s interface.
