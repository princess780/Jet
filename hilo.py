def is_palindrome(s):
    """Check if the given string s is a palindrome."""
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    start, end = 0, len(s) - 1
    
    while start < end:
        # If the characters don't match, it's not a palindrome
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Prompting the user for input
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
