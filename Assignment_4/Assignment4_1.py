power = lambda a:2 **a

def main():
    print("Enter number to get the power of two: ")
    value = int(input())
    ret = power(value)
    print("2 to the power of",value,"is:", ret)

if __name__ == "__main__":
    main()