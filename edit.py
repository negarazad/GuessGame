import random

def guess_number():
    print("Think of a number between 1 and 10.")
    low = 1
    high = 10
    attempts = 4

    for attempt in range(attempts):
        guess = random.randint(low, high)
        print(f"Attempt {attempt + 1}: Is your number {guess}?")
        
        response = input("Enter 0 if your number is higher, 1 if your number is lower, or press Enter if the guess is correct: ").lower()
        
        if response == '':
            print("Yay! The computer guessed your number correctly!")
            return
        elif response == '0':
            low = guess + 1
        elif response == '1':
            high = guess - 1
        else:
            print("Invalid input. Please enter 0, 1, or press Enter if the guess is correct.")

    print("The computer couldn't guess your number within 4 attempts. Better luck next time!")

# اجرای بازی
guess_number()
