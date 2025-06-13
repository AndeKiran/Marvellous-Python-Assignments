def main():
    data = []
    print("Enter 5 numbers:")
    #data = input()
    for i in range(5):
        data.append(int(input()))

    ans = data[0]
    for no in data:
        if(ans<no):
            ans = no

    print("Maximum number: ", ans)

if __name__ == "__main__":
    main()