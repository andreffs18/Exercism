import threading


class BankAccount(object):

    OPEN = "open"
    CLOSED = "closed"

    def __init__(self):
        self.status = self.OPEN
        self.balance = 0
        self.mutex = threading.Lock()

    def get_balance(self):
        if self.status == self.CLOSED:
            raise ValueError("Account is not open!")

        return self.balance

    def open(self):
        self.status = self.OPEN

    def deposit(self, amount):
        with self.mutex:
            # validate if account is open
            if self.status == self.CLOSED:
                raise ValueError("Account is not open!")

            # validate if amount is valid (positive integer)
            if not isinstance(amount, int) or amount < 0:
                raise ValueError("Invalid Amount: should be a non-negative integer.")

            self.balance += amount

    def withdraw(self, amount):
        with self.mutex:
            # validate if account is open
            if self.status == self.CLOSED:
                raise ValueError("Account is not open!")
            
            # validate if amount is valid (positive integer)
            if not isinstance(amount, int) or amount < 0:
                raise ValueError("Invalid Amount: should be a non-negative integer.")

            # validate that we can withdraw that amount from balance
            if amount > self.get_balance():
                raise ValueError("Invalid Amount: can't withdraw more that you have.")

            self.balance -= amount

    def close(self):
        self.status = self.CLOSED
