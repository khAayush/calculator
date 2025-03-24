
def main():
    print("Welcome to the calculator")
    print("\nChoose one number:\n")
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division")
    ch = int(input("Enter your number for desired operation: "))
    
# Sum of two numbers
def sum():
    num1= float(input("Enter first number: "))
    num2= float(input("Enter another number: "))
    if num1 <=0 or num2 <= 0:
        res = num1-num2
    
    else:
        res = num1+num2
    print(f"The sum is {res}")
sum()
