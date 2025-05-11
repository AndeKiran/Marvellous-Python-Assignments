def ChkNum(no): #Function to check entered number is even or odd
    if ((no%2) == 0):
        print( no,"is Even number")
    else:
        print( no,"is odd number")

def main(): #main function
    print("Enter number to check if its Even or Odd: ")
    try:
        value = int(input()) #stores input value from user
        ChkNum(value) #call to ChkNum userdefined function
    except ValueError:
        print("Entered data is incorrect, only integer number is allowed")    

if __name__ == "__main__":
    main()