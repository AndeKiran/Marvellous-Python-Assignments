def chkNum(no): #Function to check if entered number is divisible by 5
    if((no%5) == 0):
        return True
    else:
        return False

def main():
    print("Enter number to check if it's divisible by 5: ")
    try:
        value = int(input()) #Stores value entered by user
        result = chkNum(value)
        print(result)
    except ValueError:
        print("Entered data is incorrect, only integer number are allowed")   

if __name__ == "__main__":
    main()