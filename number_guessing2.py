import random

EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0
# Function to check  answer
def check_ans(user_guess, actual_ans,turns):
    if user_guess > actual_ans:
        print("too high")
        return turns - 1
    elif user_guess < actual_ans:
        print("too low")
        return turns - 1
    else:
        print(f"You got it! ")
        return 0

# Function to set difficulty level

def set_difficulty():
    level = str(input("type your difficulty level: 'easy' or 'hard': \n"))

    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    #  Choosing a random number between 1 and 100.
    answer = random.randint(1, 100)
    print(f"The number choose is {answer}")


    turns = set_difficulty()
    print(f"You have {turns} attempts to guess the right answer")

    # Repeat the guessing functionality if they get it wrong.

    guess = -1
    while guess != answer:

        guess = int(input("guess number: "))
        turns = check_ans(guess, answer, turns)

        if turns == 0 and guess != answer:
            print(f"You've run out of guesses. The number was {answer}. You lose.")
        else:
            print(f"You have {turns} attempts remaining. Try again.")

game()