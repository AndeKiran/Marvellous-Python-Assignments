def main():
    i = 0
    j = 0
    while(i<101):
        if(i%2==0):
            j = j + i
        i = i + 1
    print("Sum of even numbers between 1 to 100 is: ",j)

if __name__ == "__main__":
    main()