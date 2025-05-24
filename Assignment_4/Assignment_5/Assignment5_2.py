def main():
    value = input("Enter a character: ")
    if(value.isalpha() and len(value) < 1):
        if value == "a" or value == "e" or value == "i" or value == "O" or value == "u":
            print(value+" is a vowel")
        else:
            print(value+" is a consonant")
    else:
        print("Please enter single Alphabet character only")
if __name__ == "__main__":
    main()