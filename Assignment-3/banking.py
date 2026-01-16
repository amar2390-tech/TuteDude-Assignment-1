def check_balance():
    print("Your current balance is:", Balance)
def deposit_amount(amount):
    global Balance
    if amount >= 0:
        Balance += amount
    else:
        print("Invalid deposit amount.")
def withdraw_amount(amount):
    global Balance
    if amount <= 0:
        print("Cannot withdraw nagative or zero amount.")
    elif amount > Balance:
        print("Insufficient balance.")
    else:
        Balance -= amount

Balance = 0.0

while True:
    print("Welcome to the Banking System")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = input("Please select an option (1-4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amt = float(input("Enter amount to deposit: "))
        deposit_amount(amt)

    elif choice == '3':
        amt = float(input("Enter amount to withdraw: "))
        withdraw_amount(amt)

    elif choice == '4':
        print("Thank you for using the Banking System. Goodbye!")
        break
    else:
        print("Invalid option selected. Please try again.")