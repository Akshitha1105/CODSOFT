# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function for the calculator
def calculator():
    print("Simple Calculator")

    # Taking user input for the numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Displaying operation choices
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking user input for the operation choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Performing the appropriate calculation based on the user's choice
    if choice == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of division is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
