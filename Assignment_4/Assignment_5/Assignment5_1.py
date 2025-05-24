def main():
    try:
        value1 = int(input("Enter first number: "))
        value2 = int(input("Enter second number: "))

        Sum = value1 + value2
        print("Sum: ",Sum)
        Difference = value1 - value2
        print("Sum: ",Difference)
        Product = value1 * value2
        print("Sum: ",Product)
        Division = value1 / value2
        print("Sum: ",Division)
    except ValueError:
        print("Enter Integer number only")

if __name__ == "__main__":
    main()