def main():
    print("Enter a number:")
    no = int(input())
    ans = 1
    for i in range(1,no+1):
        ans = ans * i
    print("Factorial of",no,"is:",ans)

if __name__ == "__main__":
    main()