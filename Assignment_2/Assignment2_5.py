def main():
    print("Enter number to check if its prime number or not")
    value = int(input())
    for a in range(1,value+1):
        if(value%a == 0 and (a!=1 or a!=value)):
            print("Number is prime")
        else:
            print("Number is not prime")

if __name__ == "__main__":
    main()