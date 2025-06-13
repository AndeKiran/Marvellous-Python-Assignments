Double = lambda data: data * 2

def main():
    data = []
    print("Enter size of list")
    size = int(input())
    print("Enter list")
    for i in range(size):
        data.append(int(input()))

    ret = list(map(Double,data))

    print("Double list: ", ret)

if __name__ == "__main__":
    main()