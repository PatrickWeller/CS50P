def main():
    name = input("What's your name? ")
    print(hello(name))   # changed line

def hello(to="world"):
    return f"hello, {to}"   #changed line


if __name__ == "__main__":
    main()

