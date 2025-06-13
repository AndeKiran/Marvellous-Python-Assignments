from functools import reduce

Multiply = lambda a,b:a*b

def main():
    print("Enter size:")
    size = int(input())

    print("Enter number list:")
    data = []

    for i in range(size):
        data.append(int(input()))

    ret = reduce(Multiply,data)

    print("Product:", ret)

if __name__ == "__main__":
    main()