from datetime import datetime
transactions = []

def display_menu():
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Check balance")
    print("4. Check spending pattern")
    print("5. Exit")

def add_transaction():
    date = input("Date: ")

    print("1. Income")
    print("2. Expense")
    pick = input("Choose a transaction type: ")

    if pick == '1':
        transaction_type = 'Income'
    elif pick == '2':
        transaction_type = 'Expense'
    else:
        print("Invalid choice.")
        return None

    category = input("Category: ")
    description = input("Description: ")

    while True:
        try:
            amount = int(input("Amount: "))

            if amount <= 0:
                print("Enter a positive number.")
                continue
            break

        except ValueError:
            print("Invalid amount. Enter a valid number")

    transaction = {
        "date": date,
        "type": transaction_type,
        "category": category,
        "description": description,
        "amount": amount,
    }
    return transaction

def view_transactions():
    for index, transaction in enumerate(transactions, start = 1):
        print(f'{index}. {transaction["type"]}, {transaction["amount"]}, {transaction["category"]}, {transaction["description"]}, {transaction["date"]}')

def check_balance():
     balance = 0
     for transaction in transactions:
         if transaction['type'] == 'Income':
             balance += transaction['amount']
         elif transaction['type'] == 'Expense':
             balance -= transaction['amount']
     return balance

def check_spending_pattern():
    monthly_spending = {}
    today = datetime.now()
    current_month = today.month
    previous_month_count = 0

    for transaction in transactions:
        parts = transaction['date'].split('/')
        month = int(parts[1])

        if transaction['type'] == 'Expense':
            if month in monthly_spending:
                monthly_spending[month] += transaction['amount']
            else:
                monthly_spending[month] = transaction['amount']

    for month in monthly_spending:
        if month != current_month:
            previous_month_count += 1

    current_spending = monthly_spending.get(current_month, 0)
    average_monthly_spending = (sum(monthly_spending.values()) - current_spending)/ previous_month_count
    percentage = (current_spending / average_monthly_spending) * 100
    difference = percentage - 100

    if difference < 0:
        print(f'Your spending is {abs(difference)}% less than usual')
    else:
        print(f'Your spending is {difference}% greater than usual')

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        transactions.append(add_transaction())

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        print(f' Your balance is {check_balance()}')

    elif choice == "4":
        check_spending_pattern()

    elif choice == "5":
        break