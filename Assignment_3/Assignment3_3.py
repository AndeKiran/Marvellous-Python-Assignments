def main():
    print("Enter size of numbers to be entered:")
    try:
        size = int(input()) #accept N number
        data = []
        print("Enter",size,"numbers one after the other")
        
        for no in range(size): #for loop to accept N number of integers and store it in list
            data.append(int(input()))
    
        print("Entered values are:",data) #Display list of entered values
        compare = data[0]
        for no1 in data: #for loop to iterate over data entered by user
            if(int(no1) < compare): #logic to compare values and find minimum among all entered data
                compare = no1
        print("Minimum number from the above list is",compare)
    except ValueError:
        print("Invalid data, please enter integer only")

if __name__ == "__main__":
    main()