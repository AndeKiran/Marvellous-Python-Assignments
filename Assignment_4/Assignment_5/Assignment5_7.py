def main():
    length = float(input("Enter Length of rectangle: "))
    width = float(input("Enter width of rectangle: "))

    area = length * width
    print("Area", area)
    perimeter = (length + width) * 2
    print("Perimeter", perimeter)

if __name__ == "__main__":
    main()