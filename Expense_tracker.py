import csv

participants = {}


def add_participants():
    participants.clear()
    num_participant = int(input("Enter the number of participants: "))
    for _ in range(num_participant):
        name = input("Enter participants name: ")
        participants[name] = 0
    print("Participants added successfully.")


def add_expense():
    paid_by = input("Paid by: ")
    amount = float(input("Amount: "))
    distributed_amongst = input("Distributed amongst (comma separated): ").split(',')

    share = amount / len(distributed_amongst)

    participants[paid_by] += amount

    for name in distributed_amongst:
        name = name.strip()
        participants[name] -= share

    print("Expense added successfully.")


def show_participants():
    print("Participants:")
    for participant in participants:
        print(participant)


def show_expenses():
    print("Expenses:")
    participant = "Participant's Name"
    owes_gets_back = "Amount Owes/Gets Back"
    print(f"{participant:<25} {owes_gets_back:<10}")

    for participant, amount in participants.items():
        owes_gets_back = amount - sum(participants.values()) / len(participants)
        print(f"{participant:<25} {owes_gets_back:+10}")


def write_to_csv():
    with open('expenses.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Participant', 'Amount'])
        for participant, amount in participants.items():
            csvwriter.writerow([participant, amount])


while True:
    print("\nMenu:")
    print("1. Add participant(s)")
    print("2. Add expense")
    print("3. Show all participants")
    print("4. Show expenses")
    print("5. Exit/Export")

    choice = input("Select an option: ")

    if choice == '1':
        add_participants()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        show_participants()
    elif choice == '4':
        show_expenses()
    elif choice == '5':
        write_to_csv()
        print("Data exported to 'expenses.csv' successfully. Exiting the program.")
        break
    else:
        print("Invalid option. Please choose a valid option from the menu.")

