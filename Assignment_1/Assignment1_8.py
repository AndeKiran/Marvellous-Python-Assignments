def main():
    print("Enter number to print that number of * on screen: ")
    try:
        value = int(input())
        for n in range(value): #loop to iterate and print * for n number of time given by user
             print("*", end=" ") #used end parameter to override the print by default newline output to same line output
    except ValueError:
            print("Entered data is incorrect, only integer number are allowed")

if __name__ == "__main__":
     main()   