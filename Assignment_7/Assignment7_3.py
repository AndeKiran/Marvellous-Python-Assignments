Even = lambda data: data%2 == 0

def main():
    print("Enter size:")
    size = int(input())
    data= []
    print("Enter list of numbers:")
    for i in range(size):
        data.append(int(input()))

    ret = list(filter(Even,data))
    print("Even numbers: ", ret)

if __name__ == "__main__":
    main()