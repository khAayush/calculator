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

# Sum of two numbers
def sum():
    num1= float(input("Enter first number: "))
    num2= float(input("Enter another number: "))
    if num1 <=0 or num2 <= 0:
        res = num1-num2
    
    else:
        res = num1+num2
    print(f"The sum is {res}")


def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        result = num1 / num2
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Division operation completed.")

# Run the function
divide_numbers()


def sub_two_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The sub is:", num1-num2)

def main():
    print("Welcome to the calculator")
    print("\nChoose one number:\n")
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Modulus")
    ch = int(input("Enter your number for desired operation: "))
    if ch == 1:
        sum()
    elif ch ==2:
        sub_two_numbers()
    elif ch == 3:
        multiply_numbers()
    elif ch == 4:
        divide_numbers()
    elif ch == 5:
        modulus()
    else:
        print("Invalid Choice")
        
main()