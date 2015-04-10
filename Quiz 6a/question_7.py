__author__ = 'xyang'


class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0

        pass

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount

        pass

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """

        self.balance -= amount

        if self.balance < 0:
            self.balance -= 5
            self.fees += 5
        pass
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
        pass
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees
        pass


if __name__ == "__main__":
    print "aa"
    n = 127834876
    while n >= 0:
        print n
        n /= 2