import random
import game_data
import art
logo = art.logo

from game_data import data
print(logo)
#generate the random account from the data
def random_acc(account):
   account_name = account['name']
   account_description = account['description']
   account_country = account['country']
   return f"{account_name} a {account_description} from {account_country}"

#function compare and dicide the answer
def compare_foll(guess, follower_account_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"

is_game_continued = False


while not is_game_continued:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {random_acc(account_a)} ")
    print(vs)
    print(f"Compare B : {random_acc(account_b)} ")

    # guess the answer
    guess = input("guess the answer : type 'a' or 'b' \n")

    # accessing the followers
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']
    print(follower_count_a)
    print(follower_count_b)

    is_correct = compare_foll(guess, follower_count_a, follower_count_b)
    # Function to count number of attempts
    score = 0
    if is_correct:
        score += 1
        print(f"You got it. current score is {score}")
    else:
        print(f"you losed!. current score is {score}")
        is_game_continued = True
    #loop