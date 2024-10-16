def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))

def square(n):
    return n + n        # can make purposefully wrong by making n + n

if __name__ == "__main__":
    main()
