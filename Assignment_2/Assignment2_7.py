def main():
    print("Enter number to print number pattern: ")
    value = int(input())
    if(value <= 0):
        print("Enter number greater than zero to see the pattern printed")
    else:    
        for a in range(value):
            for b in range(1,value+1):
                print(b,end = " ")
                if(b ==  value):
                    print()

if __name__ == "__main__":
    main()