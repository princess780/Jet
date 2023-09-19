#Guessing game

import random

def get_user_guess():
    """Prompt the user to enter their guess and return it."""
    try:
        return int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

def check_guess(guess, target):
    """Compare the guess to the target number and return a hint or success message."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Congratulations! You've guessed the number!"

def main():
    """Main function to run the guessing game."""
    number_to_guess = random.randint(1, 100)
    guess = None
    
    print("Welcome to the Guessing Game!")
    
    while guess != number_to_guess:
        guess = get_user_guess()
        
        # If the guess is valid (not None), check and provide feedback
        if guess is not None:
            feedback = check_guess(guess, number_to_guess)
            print(feedback)

main()
