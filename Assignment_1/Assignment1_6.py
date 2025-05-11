def main():
    print("Enter number: ")
    try: #try except to validate data and handle exception
        value = int(input())
        if(value > 0): #if else condition to verify the entered number
            print("Entered number is positive")
        elif(value == 0):
            print("Entered number is Zero")
        else:
            print("Entered number is negative")
    except ValueError:
        print("Entered data is incorrect, only integer number are allowed")   

if __name__ == "__main__":
    main()