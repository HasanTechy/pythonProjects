import random

def guess_the_number():
    random_number = random.randint(1, 100)
    guess_counter = 0

    while True:
        users_guess = int(input("Guess the number from 1-100: "))
        guess_counter += 1

        if users_guess < 1 or users_guess > 100:
            print("Number is out of range (1-100)")
        elif users_guess > random_number:
            print("Too high!")
        elif users_guess < random_number:
            print("Too low!")
        elif users_guess == random_number:
            print("You hit the spot!")
            break

    print("Number of guesses:", guess_counter)


# Call the function to start the guessing game
guess_the_number()
