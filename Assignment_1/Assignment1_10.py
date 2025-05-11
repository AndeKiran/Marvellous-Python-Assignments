def main():
    print("Enter your name: ")
    value = input()
    if value.isalpha(): #function to check if entered value contains only alphabets
        print(len(value)) #len function to calculate the entered string length from user
    else:
        print("Name should only contains alphabets")

if __name__ == "__main__":
    main()