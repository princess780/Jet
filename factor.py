#Calculating Factorial

def calculate_factorial(n):
    """Return the factorial of n."""
    result = 1
    current_number = 1
    while current_number <= n:
        result *= current_number
        current_number += 1
    return result

# Prompting the user for input
try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        factorial_value = calculate_factorial(n)
        print(f"The factorial of {n} is: {factorial_value}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

