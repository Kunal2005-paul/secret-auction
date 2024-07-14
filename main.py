# from replit import clear      # it runs in replit only
import os
from art import logo


bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What is your bid?: ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # clear()   # it runs in replit only
        os.system("cls")    # for cleaning the terminal


"""
FAQ: My console doesn't clear()
This will happen if you're using an IDE other than replit. 

"""
