square = lambda a:a*a
cube = lambda a:a*a*a

def main():
    print("Enter a number:")
    try:
        no = int(input())
        sqans = square(no)
        cubans = cube(no)
        print("Square: ",sqans)
        print("Cube: ",cubans)
    except ValueError as vobj:
        print("Enter only integer values: ", vobj)

if __name__ == "__main__":
    main()