def calculator(num1, num2):
    
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    print("\nResults:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    
    try:
        division = num1 / num2
        print(f"Division: {num1} ÷ {num2} = {division}")
    except ZeroDivisionError:
        print("Division: Error - Cannot divide by zero")

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        calculator(num1, num2)
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()
