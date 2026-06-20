from account import Account

CUSTOMER_FILE = "customers.txt"
TRANSACTION_FILE = "transactions.txt"


def save_accounts(accounts):
    with open(CUSTOMER_FILE, "w") as file:
        for acc in accounts.values():
            file.write(
                f"{acc.account_number},"
                f"{acc.customer_name},"
                f"{acc.mobile_number},"
                f"{acc.account_type},"
                f"{acc.balance}\n"
            )


def load_accounts():
    accounts = {}

    try:
        with open(CUSTOMER_FILE, "r") as file:
            for line in file:
                data = line.strip().split(",")

                acc = Account(
                    int(data[0]),
                    data[1],
                    data[2],
                    data[3],
                    float(data[4])
                )

                accounts[acc.account_number] = acc

    except FileNotFoundError:
        pass

    return accounts


def save_transaction(acc_no, transaction):
    with open(TRANSACTION_FILE, "a") as file:
        file.write(f"{acc_no} - {transaction}\n")


def show_transactions(acc_no):
    try:
        with open(TRANSACTION_FILE, "r") as file:
            found = False

            for line in file:
                if line.startswith(str(acc_no)):
                    print(line.strip())
                    found = True

            if not found:
                print("No transactions found.")

    except FileNotFoundError:
        print("Transaction file not found.")