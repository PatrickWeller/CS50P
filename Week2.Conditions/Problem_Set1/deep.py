# deep.py

# In deep.py, implement a program that prompts the user for the answer to
# the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
# Otherwise output No.

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
