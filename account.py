class Account:
    MIN_BALANCE = 500

    def __init__(self, account_number, customer_name, mobile, acc_type, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.mobile = mobile
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if self.balance - amount < Account.MIN_BALANCE:
            raise ValueError(
                f"Minimum balance of ₹{Account.MIN_BALANCE} must be maintained"
            )
        self.balance -= amount

    def check_balance(self):
        return self.balance
    def update_details(self, name, mobile):
        if name.strip():
            self.customer_name = name
        if mobile.strip():
            self.mobile = mobile