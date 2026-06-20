from account import Account
from file_handler import *

accounts = load_accounts()

def create_account():
    acc_no = int(input("Enter Account Number: "))
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter Name: ")
    if not name.strip():
        print("Name cannot be empty")
        return
    while True:
        mobile = input("Enter Mobile Number: ")
        if mobile.isdigit() and len(mobile) == 10:
            break
        else:
            print("Invalid Mobile Number")
    acc_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Initial Balance: "))
    if balance < Account.MIN_BALANCE:
        print("Minimum balance must be ₹500")
        return
    acc = Account(acc_no, name, mobile, acc_type, balance)
    accounts[acc_no] = acc
    save_accounts(accounts)
    print("Account Created Successfully")

def display_account():
    try:
        acc_no = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid Account Number")
        return
    if acc_no in accounts:
        acc = accounts[acc_no]
        print("\n--- Account Details ---")
        print(f"Account Number : {acc.account_number}")
        print(f"Name           : {acc.customer_name}")
        print(f"Mobile Number  : {acc.mobile}")
        print(f"Account Type   : {acc.acc_type}")
        print(f"Current Balance: ₹{acc.check_balance()}")
        print("-----------------------")
    else:
        print("Account not found")

def deposit_money():
    acc_no = int(input("Enter Account Number: "))
    if acc_no not in accounts:
        print("Account not found")
        return
    try:
        amount = float(input("Enter Amount: "))
        accounts[acc_no].deposit(amount)
        save_transaction(acc_no, f"Deposited ₹{amount}")
        save_accounts(accounts)
        print("Deposit Successful")
    except ValueError as e:
        print(e)

def withdraw_money():
    acc_no = int(input("Enter Account Number: "))
    if acc_no not in accounts:
        print("Account not found")
        return

    try:
        amount = float(input("Enter Amount: "))
        accounts[acc_no].withdraw(amount)
        save_transaction(acc_no, f"Withdrawn ₹{amount}")
        save_accounts(accounts)
        print("Withdrawal Successful")
    except ValueError as e:
        print(e)

def check_balance():
    acc_no = int(input("Enter Account Number: "))
    if acc_no in accounts:
        print("Balance: ₹", accounts[acc_no].check_balance())
    else:
        print("Account not found")

def update_account():
    acc_no = int(input("Enter Account Number: "))
    if acc_no not in accounts:
        print("Account not found")
        return
    name = input("New Name: ")
    mobile = input("New Mobile: ")
    accounts[acc_no].update_details(name, mobile)
    save_accounts(accounts)
    print("Details Updated Successfully")

def delete_account():
    acc_no = int(input("Enter Account Number: "))
    if acc_no in accounts:
        del accounts[acc_no]
        save_accounts(accounts)
        print("Account Deleted")
    else:
        print("Account not found")

def transaction_history():
    acc_no = int(input("Enter Account Number: "))
    show_transactions(acc_no)
while True:
    print("\n==========================")
    print("     BANK MANAGEMENT")
    print("==========================")
    print("1. Create Account")
    print("2. Display Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Update Account")
    print("7. Delete Account")
    print("8. Transaction History")
    print("9. Exit")
    print("==========================")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        display_account()
    elif choice == "3":
        deposit_money()
    elif choice == "4":
        withdraw_money()
    elif choice == "5":
        check_balance()
    elif choice == "6":
        update_account()
    elif choice == "7":
        delete_account()
    elif choice == "8":
        transaction_history()
    elif choice == "9":
        print("Thank You for Using Bank Management System")
        break
    else:
        print("Invalid Choice")