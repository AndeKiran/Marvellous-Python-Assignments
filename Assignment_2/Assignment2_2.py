def main():
    print("Enter one number to print * in number of row's & column's of entered number")
    value1 = int(input())
    for a in range(value1):
        for b in range(value1):
            print("*", end=" ")
            if (b == (value1 - 1)):
                print(end="\n")
        
if __name__ == "__main__":
    main()