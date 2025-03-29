

def find_highest_bid(bid_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bid_dictionary:
        bid_amt = bid_dictionary[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder

    print(f"The winner is {winner}")


bid = {}
bid_continue = True
while bid_continue:
    name = str(input("Enter your name: \n"))
    bid_amt = int(input("Enter your bid amount: \n"))
    bid[name] = bid_amt
    any_bidder = input("Any other person is there want to bid? y for yes and n for no: \n")
    if any_bidder == "n":
        bid_continue = False
        find_highest_bid(bid)
    else:
        print( "\n" * 20)


