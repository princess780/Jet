#Sum of even numbers

def sum_even_numbers(n):
    """Return the sum of all even numbers from 1 to n."""
    sum_even = 0
    current_number = 1
    while current_number <= n:
        if current_number % 2 == 0:
            sum_even += current_number
        current_number += 1
    return sum_even

# Prompting the user for input
try:
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        result = sum_even_numbers(n)
        print(f"The sum of all even numbers from 1 to {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")

