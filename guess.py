import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 50.")
print("Try to guess it in as few attempts as possible.\n")

number = random.randint(1, 50)
guess = int(input("Take a guess: "))
tries = 1

while guess != number:
    if guess > number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it!  The number was", number)
print("And it only took you", tries, "tries!\n")
