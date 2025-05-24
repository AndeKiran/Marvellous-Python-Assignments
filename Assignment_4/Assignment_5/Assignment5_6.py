def main():
    try:
        c = float(input("Enter temperature is Celsius: "))
        F = (c * 9/5) + 32
        print("Temperature in Fahrenheit: ", F)
    except ValueError:
        print("Enter only number either interger or float")

if __name__ == "__main__":
    main()