# Importing the necessary packages
import random

# Generating a random number and setting the guessing limit
secret_number = random.randint(1, 10)
guess_limit = 3

# Function to welcome the user
def welcome_user():
    print("Welcome to the Number Guessing Game!")
    print("You have", guess_limit, "attempts to guess the correct number between 1 and 10.")

# Recursive function for guessing the number
def guess_number(attempts):
    if attempts == 0:
        print("Sorry, you've used all your attempts. The correct number was", secret_number)
        return
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        return
    else:
        print("Incorrect guess. Try again.")
        guess_number(attempts - 1)

# Function for executing the game
def play_game():
    welcome_user()
    guess_number(guess_limit)

# Printing memory address of the secret number
print("Memory address of the secret number:", id(secret_number))

# Exercise: Find the First Repeating Character and Print its Memory Address
def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            print("First repeating character:", char, "Memory address:", id(char))
            return char
        char_count[char] = 1
    return None

sample_string = "hello world"
find_first_repeating_character(sample_string)
