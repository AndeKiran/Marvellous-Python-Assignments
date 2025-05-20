def main():
    print("Enter number to print * in triange pattern:")
    value = int(input())
    no = value
    for a in range(value):
        for b in range(no):
            print("*",end = " ")
            if(b == no-1):
                print()
        no = no - 1        

if __name__ == "__main__":
    main()