try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num1 = int(num1)
    num2 = int(num2)
    sum_result = num1 + num2
    print("Sum:", sum_result)
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        division_result = num1 / num2
        print("Division:", division_result)
except ValueError:
    print("Invalid input")