def main():
    print("Entner number to get its factorial: ")
    value1 = int(input())
    no=1
    for b in range(1,value1+1):
        no = no * b
    print("Factorial of number",value1,"is: ",no)

if __name__ == "__main__":
    main()