def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    smiles = convert(input())
    print(smiles)

main()

