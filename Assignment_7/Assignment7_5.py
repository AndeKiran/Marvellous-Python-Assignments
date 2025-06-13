def main():
    value = input("Enter a string: ")
    size =  len(value) - 1
    for i in range(len(value)):
        if(i < size):
            if(value[i] == value[size]):
                size = size - 1
            else:
                print(value, "is not a palindrome")
                break
        else:
            print(value,"is a palindrome")
            break
            
if __name__ == "__main__":
    main()