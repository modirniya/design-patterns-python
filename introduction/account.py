class Account:

    def __init__(self, balance: float):
        self._balance = balance

    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print('Amount: %s has successfully been added' % amount)
            print(self)
        else:
            print('Invalid amount, must be positive')

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            print('Amount: %s has successfully been withdrawn' % amount)
            print(self)
        else:
            print('Inefficient funds, please deposit accordingly')

    def __str__(self) -> str:
        return 'Balance: %s' % self._balance
