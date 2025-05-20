def main():
    print("Enter size of numbers to be entered:")
    try:
        size = int(input()) #accept N number
        data = []
        print("Enter",size,"numbers one after the other")
        
        for no in range(size): #for loop to accept N number of integers and store it in list
            data.append(int(input()))
    
        print("Entered values are:",data) #Display list of entered values
        print("Element to search: ") 
        searchNo = int(input()) #accept element from user to search the occurance in list accepted by user
        count = 0
        for no1 in data: #for loop to iterate over data entered by user
            if(int(no1) == searchNo): #logic to search n count occurance of value given by user among all entered data
                count = count + 1
        print("Occurance of entered element in above list is:",count)
    except ValueError:
        print("Invalid data, please enter integer only")

if __name__ == "__main__":
    main()