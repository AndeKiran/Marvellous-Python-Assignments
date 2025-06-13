def main():
    print("Enter a number: ")
    no = int(input())
    if(no == 1):
        print("Enter number greater than 1")
    else:    
        for i in range(2,no+1):
            if(no%i == 0):
                if(i != no):
                    print("Number is not prime")
                    break
                else:
                    print("Number is prime")
                    break
            

if __name__ == "__main__":
    main()