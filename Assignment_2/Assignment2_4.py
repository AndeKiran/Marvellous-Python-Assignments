def main():
    print("Enter number, to see the factors of that number and total sum of factors")
    value = int(input())
    factors = []
    no = 0
    for a in range(1,value):
        if(value%a == 0):
            factors.append(a)
            no=no+a
    print("Factors of number",value,"are: ",factors)
    print("Addition of all above factors is: ",no)


if __name__ == "__main__":
    main()