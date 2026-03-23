import threading


class BankAccount(object):
    """
    A thread-safe bank account implementation with basic operations.

    This class provides basic banking operations including deposits, withdrawals,
    and balance inquiries. All operations are thread-safe using mutex locking.
    """

    OPEN = "open"
    CLOSED = "closed"

    def __init__(self) -> None:
        """
        Initialize a new BankAccount with zero balance and open status.
        """
        self.status = None
        self.balance = 0
        self.mutex = threading.Lock()

    def get_balance(self) -> int:
        """
        Get the current balance of the account.

        Returns:
            int: The current balance of the account.

        Raises:
            ValueError: If the account is closed.
        """
        if self.status == self.CLOSED:
            raise ValueError("Account is not open!")

        return self.balance

    def open(self) -> None:
        """
        Open the bank account.

        Sets the account status to OPEN, allowing deposits and withdrawals.
        """
        if self.status == self.OPEN:
            raise ValueError("Account already opened!")
        self.status = self.OPEN

    def deposit(self, amount: int) -> None:
        """
        Deposit money into the account.

        This operation is thread-safe using mutex locking.

        Args:
            amount (int): The amount to deposit. Must be a non-negative integer.

        Raises:
            ValueError: If the account is closed or if amount is invalid
                       (negative or not an integer).
        """
        with self.mutex:
            # validate if account is open
            if self.status == self.CLOSED:
                raise ValueError("Account is not open!")

            # validate if amount is valid (positive integer)
            if not isinstance(amount, int) or amount < 0:
                raise ValueError("Invalid Amount: should be a non-negative integer.")

            self.balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Withdraw money from the account.

        This operation is thread-safe using mutex locking.

        Args:
            amount (int): The amount to withdraw. Must be a non-negative integer.

        Raises:
            ValueError: If the account is closed, if amount is invalid
                       (negative or not an integer), or if there are insufficient funds.
        """
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

    def close(self) -> None:
        """
        Close the bank account.

        Sets the account status to CLOSED, preventing further transactions.
        """
        if self.status is None:
            raise ValueError("Account needs to be opened first!")
        if self.status == self.CLOSED:
            raise ValueError("Account already closed!")
        self.status = self.CLOSED
        self.balance = 0
