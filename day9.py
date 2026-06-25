def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculator():
    print("=== Secure Calculator ===")
    
    try:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        print(f"Addition: {num1 + num2}")
        print(f"Subtraction: {num1 - num2}")
        print(f"Multiplication: {num1 * num2}")
        print(f"Division: {divide(num1, num2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Calculator closed.")

calculator()