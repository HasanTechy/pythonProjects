# ---------------------------
def start_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter ur option: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answers(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# ---------------------------
def check_answers(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("wrong!")
        return 0


# ---------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Results")
    print("-------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses / len(questions) * 100)
    print("ur score: " + str(score) + "%")


# ---------------------------
def play_again():
    response = input("Wanna play one more time? (yes/no)").upper()
    if response == "YES":
        return True
    else:
        return False


# ---------------------------

questions = {"Who created the game?: ": "A",
             "What is the date of creation?: ": "B"}

options = [["A. Me", "B. Not me"],
           ["A. today", "B. yesterday"]]

start_game()

while play_again():
    start_game()

print("BYE!")
