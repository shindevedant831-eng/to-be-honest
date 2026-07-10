
A = int(input("Enter a first number: "))
B = int(input("Enter a second number: "))

C = int(input("enter 1.add, 2.sub, 3.multiply, 4.divide: "))

match C:
    case 1:
        D = A + B
        print(f"A + B = {D}")
    case 2:
        D = A - B
        print(f"A - B = {D}")
    case 3:
        D = A * B
        print(f"A * B = {D}")
    case 4:
        if B != 0:
            D = A / B
            print(f"A / B = {D}")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Please enter a valid number.")
