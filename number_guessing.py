import random

num = random.randint(1, 100)
choose = input("Choose the level easy or hard: \n ")
easy, hard = 10, 5
game_ended = False

while not game_ended:
    if easy == 0 or hard == 0:
        print("You losed and game ended")

    ans = int(input("guess the correct answer: \n "))


    if  choose == "easy":
        print(f"number of attempts: {easy}")
        if num > ans:
            print("Too low")
            easy -= 1
        elif num < ans:
            print("Too high")
            easy -= 1
        elif num == ans:
            print("You win")
            break

    else:
        print(f"number of attempts : {hard}")
        if num > ans:
            print("Too low")
            easy -= 1
        elif num < ans:
            print("Too high")
            easy -= 1
        elif num == ans:
            print("You win")
            break
