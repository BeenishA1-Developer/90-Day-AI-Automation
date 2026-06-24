import random

secret = random.randint(1, 10)
chances = 3

print("=== Number Guessing Game ===")
print(f"Guess the number between 1 and 10. You have {chances} chances.")

for attempt in range(1, chances + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    
    if guess == secret:
        print(f"Correct! You guessed it in {attempt} attempt(s)!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempt == chances:
        print(f"Game Over! The number was {secret}")