def main():
    try:
        value = int(input(("Enter the age of person: ")))
        if(value>=18):
            print("Person is eligible to vote")
        else:
            print("Person is Not eligible to vote")
    except ValueError:
        print("Please enter integer value only")

if __name__ == "__main__":
    main()