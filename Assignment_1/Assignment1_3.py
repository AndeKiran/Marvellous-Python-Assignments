def Add(no1,no2): #Function to calculate addition of two number given from user
    ans = no1 + no2
    return ans #return result to caller

def main(): #main function
    print("Enter two numbers for addition: ")
    try: #try except to validate data handle exception
        value1 = int(input()) #stores number entered from user
        value2 = int(input())
        result = Add(value1,value2) #Call to userdefined add funtion with positioned arguments
        print("Addition of two numbers is: " ,result)
    except ValueError:
        print("Entered data is incorrect, only integer number are allowed")

if __name__ == "__main__":
    main()