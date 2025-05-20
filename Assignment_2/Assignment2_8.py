def main():
    print("Enter number to print number pattern: ")
    value = int(input())
    if(value <= 0):
        print("Enter number greater than zero to see the pattern printed")
    else:    
        no = 1
        for a in range(value):
            for b in range(1,no+1):
                print(b,end = " ")
                if(b == no):
                    print()
            no = no + 1

if __name__ == "__main__":
    main()