def main():
    print("Enter multiple numbers and get its addition displayed:")
    value = input()
    add = 0
    for no in value:
        add = add + int(no)        
    print("Addition of all entered number i.e.",value,"is",add)

if __name__ == "__main__":
    main()