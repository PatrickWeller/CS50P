# coke.py

# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
# and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.

# In a file called coke.py,
# implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

def main():
    coins = 0
    while coins <= 50:
        print("Amount Due:", 50 - coins)
        coins = coins + request_coin()
    change = coins - 50
    print("Change Owed: ", change)

def request_coin():
    entered_coin = int(input("Insert Coin: "))
    match entered_coin:
        case 5 | 10 | 25 :
            return entered_coin
        case _:
            return 0

main()
