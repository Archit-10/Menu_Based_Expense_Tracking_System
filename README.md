<h1>Menu-Based Expense Tracking System</h1>

<p>Welcome to <strong>PennyWise (working title)</strong>, your straightforward, Python-powered solution for tracking group expenses. Whether you're managing a weekend getaway, a project expense report, or a casual meal with friends, PennyWise helps you keep finances clear and fair. Built with a minimal, menu-driven interface, it’s perfect for those who want a quick, transparent way to split expenses.</p>

<h2>📌 Features</h2>

<h3>Add Participants</h3>
<p>Effortlessly add multiple participants by name, each initializing with a balance of zero. This sets the groundwork for tracking each individual’s share of group expenses.</p>

<h3>Log Expenses</h3>
<p>Record expenses by specifying:</p>
<ul>
    <li><strong>The payer</strong></li>
    <li><strong>The total amount</strong></li>
    <li><strong>Participants involved in that expense</strong></li>
</ul>
<p>PennyWise then calculates each participant's share automatically, allocating costs accurately based on the input.</p>

<h3>View Participants</h3>
<p>List all participants to keep track of who's involved in the current session.</p>

<h3>Show Balance</h3>
<p>See who owes what or gets back money. PennyWise calculates each participant's balance relative to the average contribution, showing a clear picture of who needs to settle up.</p>

<h3>Export to CSV</h3>
<p>With a single click, export the expense data to <code>expenses.csv</code> for easy sharing and record-keeping.</p>

<h2>📋 Installation and Usage</h2>

<h3>Clone the Repository:</h3>
<pre>
<code>git clone &lt;repo-url&gt;
cd pennywise</code>
</pre>

<h3>Run the Program:</h3>
<pre>
<code>python Expense_tracker.py</code>
</pre>

<h3>Follow the Menu Options:</h3>
<p>The menu will prompt you through adding participants, logging expenses, viewing balances, and exporting data to a CSV file when you’re done.</p>

<h2>💡 Sample Walkthrough</h2>

<ul>
    <li>Add participants with their names.</li>
    <li>Record an expense, indicating who paid and how much, along with the participants sharing the cost.</li>
    <li>View individual balances to see who owes or gets back money.</li>
    <li>Export your expense data in a neat CSV format before exiting the program.</li>
</ul>

<h3>Example Usage</h3>
<p>Here's a quick example of how a session might look:</p>

<pre>
<code>
Menu:
1. Add participant(s)
2. Add expense
3. Show all participants
4. Show expenses
5. Exit/Export

Select an option: 1
Enter the number of participants: 3
Enter participant's name: Penny Nichols
Enter participant's name: Buck Wilde
Enter participant's name: Cash Sterling

Select an option: 2
Paid by: Penny Nichols
Amount: 60
Distributed amongst (comma separated): Penny Nichols, Buck Wilde, Cash Sterling

Expense added successfully.

Select an option: 4
Expenses:
Participant's Name           Amount Owes/Gets Back  
Penny Nichols                        +40.0
Buck Wilde                           -20.0
Cash Sterling                        -20.0
</code>
</pre>

<h2>📝 Data Export</h2>

<p>After completing all entries, export your data to a CSV file (<code>expenses.csv</code>). The file includes each participant's net balance, making it easy to share or review your finances.</p>

<h2>Challenges and Future Directions</h2>

<h3>Challenges Faced</h3>

<ul>
    <li><strong>Accurate Expense Distribution:</strong>
        <p>Handling expenses with varied participant distributions was essential to ensure accuracy. Balancing each individual's owed or paid amount against others demanded precise computation.</p>
    </li>
    <li><strong>User Interface Limitations:</strong>
        <p>Keeping the interface simple meant restricting user interaction to text-based prompts. Maintaining ease of use while providing clear instructions was a constant focus.</p>
    </li>
    <li><strong>Data Persistence:</strong>
        <p>Since the current system only writes data upon exit, handling interruptions in real-time data saving could improve reliability.</p>
    </li>
</ul>

<h3>Future Directions</h3>

<ul>
    <li><strong>Graphical User Interface (GUI):</strong>
        <p>Adding a GUI would enhance user experience by allowing interaction through buttons and menus, making PennyWise more intuitive and visually accessible.</p>
    </li>
    <li><strong>Real-Time Synchronization:</strong>
        <p>Implementing real-time data saving would prevent accidental data loss. Integration with cloud storage could enable seamless collaboration across devices.</p>
    </li>
    <li><strong>Advanced Reporting and Analysis:</strong>
        <p>Enhanced data output with summary reports, visual charts, and in-depth analysis could help users gain insights into spending patterns and balances.</p>
    </li>
    <li><strong>Mobile Compatibility:</strong>
        <p>Developing a mobile-friendly version would provide users with on-the-go expense tracking, ideal for group events and trips.</p>
    </li>
    <li><strong>Machine Learning for Predictive Insights:</strong>
        <p>Integrating basic machine learning could allow PennyWise to offer budgeting suggestions based on historical spending patterns, adding value for frequent users.</p>
    </li>
</ul>

