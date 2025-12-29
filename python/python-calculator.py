print("Python Calculator")

num1 = float(input("Enter number: "))
num2 = float(input("Enter another number: "))

print ("Choose operation (1 - 4) ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter operation: "))

if choice == 1:
    result = num1 + num2
    print("Result: ", result)
elif choice == 2:
    result = num1 - num2
    print("Result: ", result)
elif choice == 3:
    result = num1 * num2
    print("Result: ", result)
elif choice == 4:
    result = num1 / num2
    if num2 == 0:
        print("Cant divide by zero")
    else:
        print("Result: ", result)
else:
    print("Enter a number betwen 1 - 4")