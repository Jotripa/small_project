import os
from ascii import logo
print(logo)

bids = {}
bidding_finish = False

def find_highest_bidder(bidding_recoed):
    highest_bid = 0
    for bidder in bidding_recoed:
        bid_amount = bidding_recoed[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid is ${highest_bid}")
while not bidding_finish:
    name = input("Whats your name : ")
    price = int(input("How much you want to bid : $"))
    bids[name] = price
    should_cont = input("Are there any more bidder ? type 'yes' or 'no'")
    if should_cont == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_cont == "yes":
        os.system('cls')
