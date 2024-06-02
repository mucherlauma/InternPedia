# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display welcome message
def welcome_message():
    print("Welcome to Simple Calculator!")
    print("Enter 'exit' to quit.")

# Function to display farewell message
def farewell_message():
    print("Thank you for using Simple Calculator!")

# Function to get user input and perform calculation
def calculate():
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        if operation == 'exit':
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter a valid operation.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        print("Result:", result)

# Main function to run the calculator
def main():
    welcome_message()
    calculate()
    farewell_message()

if __name__ == "__main__":
    main()
