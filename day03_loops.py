# Build a number guessing game: computer picks 1–10, player guesses until correct. Show 'Too high' / 'Too low'. Count attempts.


import random

# This will let computer pick any random number between 1 and 10
secret_number = random.randint(1,10)
attempts = 0 # Initialize the attempt counter

print("Welcome to the number guessing game!\nI am thinking about a number between 1 and 10, you have to guess it.") 

# Starting the loop 
while True:
    guess = int(input("Enter your guess: "))

    attempts += 1
    
    # checking the guess
    if guess < secret_number:
        print("Too low!Tr y again")
    elif guess > secret_number:
        print("Too high! Try again")
    else:
        print(f"🎉 Correct! You found the number in {attempts} attempts.")
        break # This exits the loop and end the game