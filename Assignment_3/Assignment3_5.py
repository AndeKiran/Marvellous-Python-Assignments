from MarvellousNum import ChkPrime

def ListPrime(task,values): #function which calls ChkPrime function from inside it and iterates and passes value to ChkPrime to check prime number in the given list
    primelist = []
    for no1 in values:
       result = task(no1)
       if result == True:
           primelist.append(no1)
    return primelist

def main():
    print("Enter size of numbers to be entered:")
    try:
        size = int(input()) #accept N number
        data = []
        print("Enter",size,"numbers one after the other")
        
        for no in range(size): #for loop to accept N number of integers and store it in list
            data.append(int(input()))
    
        print("Entered values are:",data) #Display list of entered values

        primeLst = ListPrime(ChkPrime,data) #Used callback function and passed ChkPrime function from another module as argument 

        print("List of all prime numbers are:", primeLst)
        Addition = 0
        for no1 in primeLst: #for loop to do addition of all prime numbers in the list returned from ListPrime function
            Addition = Addition + no1
            print(no1, end = "+")
  
        print(" =",Addition)
    except ValueError:
        print("Invalid data, please enter integer only")

if __name__ == "__main__":
    main()