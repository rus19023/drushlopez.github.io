
import random
from random import randint
print("Welcome to the number guessing game!")
seed_value = input("Enter random seed: ")
random.seed(seed_value)
keep_playin = "yes"
num_to_guess = randint(1, 100)
guess_count = 0
while guess_count < 101:
    guess_count += 1
    print()
    the_guess = int(input("Please enter a guess: "))
    if the_guess == num_to_guess:
        print("Congratulations. You guessed it!")
        print("It took you " + str(guess_count) + " guesses.")
        print()
        guess_count = 0
        num_to_guess = randint(1, 100)
        keep_playin = input("Would you like to play again (yes/no)? ")
        if keep_playin == "no":
            print("Thank you. Goodbye.")
            break
    else:
        if the_guess > num_to_guess:
            print("Lower")
        elif the_guess < num_to_guess:
            print("Higher")
