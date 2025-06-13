from random import randint

# generate random number from 1 to 100
gen_num = randint(1, 100)

# number of tries to guess number
tries = 7

# print welcome message
print("Hi! I have thought of a number between 1 and 100. Try to guess it in 7 attempts.")

for attempt in range(1, tries + 1):
    guess = input(f"Attempt {attempt}: Enter your guess: ")

    # ensure valid input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess_num = int(guess)

    if guess_num > gen_num:
        print("Too big.")
    elif guess_num < gen_num:
        print("Too small.")
    else:
        print(f"You guessed it! The number was {gen_num}.")
        break
else:
    print(f"You've used all your tries. The number was {gen_num}.")
