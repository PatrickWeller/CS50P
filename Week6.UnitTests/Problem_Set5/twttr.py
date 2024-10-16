# twttr.py

# When texting or tweeting,
# it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr.

# In a file called twttr.py,
# implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def main():
    string = input("Input: ")
    strng = shorten(string)
    print(strng)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        word = word.replace(vowel, "")
        word = word.replace(vowel.upper(), "")
    return word

if __name__ == "__main__":
    main()
