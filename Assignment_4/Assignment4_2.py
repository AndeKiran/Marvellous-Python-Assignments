Multiply = lambda a,b: a * b

def main():
    print("Enter two number to get its multiplication: ")
    value1 = int(input("Enter First number: "))
    value2 = int(input("Enter Second number: "))
    
    ret = Multiply(value1,value2)
    print("Multiplication of",value1,"*",value2,"is:", ret)

if __name__ == "__main__":
    main()