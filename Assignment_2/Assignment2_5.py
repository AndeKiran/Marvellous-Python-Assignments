def main():
    print("Enter number to check if its prime number or not")
    value = int(input())
    if(value == 1):
        print("A prime number is a natural number greater than 1, Enter number greater than one")
    else:    
        for a in range(2,value+1):
            if(value%a == 0):
                if((a!=value)):
                    print("Number is not prime")
                    break
                else:
                    print("Number is prime")
                    break

if __name__ == "__main__":
    main()
