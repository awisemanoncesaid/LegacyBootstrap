class AccountOperations:
    def __init__(self, account_data):
        self.account_data = account_data

    def credit(self, amount):
        self.account_data.balance += amount
        return self.account_data.balance

    def debit(self, amount):
        if amount > self.account_data.balance:
            return False
        self.account_data.balance -= amount
        return True