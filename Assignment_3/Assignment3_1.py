def main():
    print("Enter size of numbers to be entered:")
    try:
        size = int(input()) #accept N number
        data = [] #declared list to store the data entered by user
        print("Enter",size,"numbers one after the other")
        
        for no in range(size): #for loop to accept N number of integers and store it in list
            data.append(int(input()))
    
        print("Entered values are:",data) #Display list of entered values
        addition = 0
        for no1 in data:  #for loop to iterate over data entered by user
            addition = addition + int(no1)  #logic of addition which does sum of all entered data
        print("Addition of all above values are:",addition)
    except ValueError:
        print("Invalid data, please enter integer only")


if __name__ == "__main__":
    main()