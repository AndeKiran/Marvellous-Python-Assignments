def main():
    print("Enter three numbers:")
    data = []
    
    for no in range(3):
        data.append(int(input()))

    ans = data[0]

    for no in data:
        if(ans < no):
            ans = no
            
    print("Largest number is: ", ans)

if __name__ == "__main__":
    main()