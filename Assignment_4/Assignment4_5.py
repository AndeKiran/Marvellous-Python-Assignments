from functools import reduce
import sys

def ChkPrime(value): #function to check given number is prime or not 
    for a in range(2,value+1):
        if(value%a == 0):
            if((a!=value)):
                #If "Number is not prime"
                return False
                break
            else:
                # If "Number is prime"
                return True
                break
    
multiBy2 = lambda b:b*2

def compare(value1,value2):
    max = value1
    if(value1 > value2):
        max = value1
    else:
        max = value2
    return max    

def main():
    data = []
    if(len(sys.argv)<3):
        print("Insufficient number of arugemts, this application needs atleast 2 numbers to perform all operations")
        print("Example Enter command as: python Assignment4_3.py 1 2 3 ... and so on ")
    else:
        try:
            for no in range(1,len(sys.argv)): # accepted list from user using sys.argv this attribute is a list that stores command-line arguments passed to a Python script. 
                data.append(int(sys.argv[no])) # used sys.argv as in problem statement it was not mentioned to accept N number from user, expected was to only accept list from user

            print("Input list: ",data)
            filteredList = list(filter(ChkPrime,data))
            mapList = list(map(multiBy2,filteredList))
            reducedList = reduce(compare,mapList)

            print("List after filter: ",filteredList)
            print("List after map: ",mapList)
            print("Output of reduce: ",reducedList)
        except TypeError as tObj:
            print("Your list should contain atleast two prime numbers", tObj)
        except ValueError as vObj:
            print("Enter only integer values, your tried entering alphabets", vObj)
if __name__ == "__main__":
    main()