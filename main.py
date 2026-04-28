def validate_numeric(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric")

def add(a, b):
    validate_numeric(a, b)
    """Add two numbers"""
    return a + b

def subtract(a, b):
    validate_numeric(a, b)
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    validate_numeric(a, b)
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    validate_numeric(a, b)
    """Divide two numbers with zero check"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("================")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
