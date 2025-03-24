def multiply_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    print("Welcome to the calculator")
    print("\nChoose one number:\n")
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division")
    ch = int(input("Enter your number for desired operation: "))
    