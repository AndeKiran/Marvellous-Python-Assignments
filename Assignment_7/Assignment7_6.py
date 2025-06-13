def prime(dataList):
    primeData = []
    for i in range(2,dataList+1):
        if(dataList%i == 0):
            if(i != dataList):
                return False
                break
            else:
                return True
            break

def main():
    print("Enter size of list:")
    size = int(input())
    print("Enter list of numbers")
    data = []
    for no in range(size):
        data.append(int(input()))

    ret = list(filter(prime,data))

    print(ret)

if __name__ == "__main__":
    main()