from functools import reduce
import sys

compare = lambda a:a>=70 and a<=90
            
increase = lambda b:b+10

multiply = lambda a,b:a*b

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
            filteredList = list(filter(compare,data))
            mapList = list(map(increase,filteredList))
            reducedList = reduce(multiply,mapList)

            print("List after filter: ",filteredList)
            print("List after map: ",mapList)
            print("Output of reduce: ",reducedList)
        except TypeError:
            print("Your list should contain atleast two such numbers which are greated than 70 and less than 90")
        except ValueError:
            print("Enter only integer values, your tried entering alphabets")
if __name__ == "__main__":
    main()