class Account:
    def __init__(self):
        self._balance = 0   # Remember _ prevents name clashses and says don't change this.

    @property
    def balance(self):
        return self._balance

    def deposit (self, n):
        self._balance += n

    def withdraw(self, n):
        self.balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

# I declared balance to be global previously, in 02_GlobalVariables,
# Then told each function it was global.
# But this use of classes means that my instance variables are accessible,
# to all methods of the class.


# Constants - variables that no one can change
# It's a good part of coding defensively.
