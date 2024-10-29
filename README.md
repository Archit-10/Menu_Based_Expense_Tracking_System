### Menu-Based Expense Tracking System


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

🚀 Challenges and Future Directions
Challenges Faced

    Accurate Expense Distribution:
        Handling expenses with varied participant distributions was essential to ensure accuracy. Balancing each individual's owed or paid amount against others demanded precise computation.

    User Interface Limitations:
        Keeping the interface simple meant restricting user interaction to text-based prompts. Maintaining ease of use while providing clear instructions was a constant focus.

    Data Persistence:
        Since the current system only writes data upon exit, handling interruptions in real-time data saving could improve reliability.
Future Directions

    Graphical User Interface (GUI):
        Adding a GUI would enhance user experience by allowing interaction through buttons and menus, making PennyWise more intuitive and visually accessible.

    Real-Time Synchronization:
        Implementing real-time data saving would prevent accidental data loss. Integration with cloud storage could enable seamless collaboration across devices.

    Advanced Reporting and Analysis:
        Enhanced data output with summary reports, visual charts, and in-depth analysis could help users gain insights into spending patterns and balances.

    Mobile Compatibility:
        Developing a mobile-friendly version would provide users with on-the-go expense tracking, ideal for group events and trips.

    Machine Learning for Predictive Insights:
        Integrating basic machine learning could allow PennyWise to offer budgeting suggestions based on historical spending patterns, adding value for frequent users.



