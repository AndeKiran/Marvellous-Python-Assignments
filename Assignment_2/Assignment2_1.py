import Arithmetic as arith

def main():
    print("Enter two numbers for addition, subtraction, multiplication & division of that numbers")
    try:
        value1 = int(input())
        value2 = int(input())
        addition = arith.Add(value1, value2)
        print("Addition of entered two numbers i.e. ",value1,"+",value2," is: ", addition)
        subtraction = arith.Sub(value1, value2)
        print("Subtraction of entered two numbers i.e. ",value1,"-",value2,"is: ", subtraction)
        multiplication = arith.Mult(value1, value2)
        print("Multiplication of entered two numbers i.e. ",value1,"*",value2,"is: ", multiplication)
        division =  arith.Div(value1, value2)
        print("Division of entered two numbers i.e. ",value1,"/",value2,"is: ", division)
    except ValueError:
            print("Entered data is incorrect, enter only integer number and hit enter after entering each number")

if __name__ == "__main__":
    main()