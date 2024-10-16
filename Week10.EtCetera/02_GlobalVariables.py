#### Global variables

# A variable set outside of my functions, near top of script,
# that might be specific to that whole file.

# bank.py
balance = 0

def main():
    print("Balance", balance)

if __name__ == "__main__":
    main()

# Variable defined outside the function, now used within it.

# See below though, I've tried to change balance within the functions.
# This will NOT work.
# UnboundLocalError: local varaible 'balance' referenced before assignment.

balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()

# It's OK to read a global variable in a function, but NOT write to it.
# balance is NOT local to the deposit or withdraw functions,
# they don't have access to it.

# We need to use the keyword "global"
alance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
