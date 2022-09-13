import random
import os
from ascii import logo
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a Draw"
    elif computer_score == 0:
        return "Lose, Computer has a blackjack"
    elif user_score == 0:
        return "You win with the blackjack"
    elif user_score > 21:
        return "Too far, You lose!"
    elif computer_score > 21:
        return "Computer went to far, You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game ():

    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range (2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are : {user_cards}, current score : {user_score}")
        print(f"Computer card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to hit, type 'n' to pass : ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards : {user_cards}, final score : {user_score}")
    print(f"Computer's final cards : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play ? 'y' for yes and 'n' for no : "):
    os.system('cls')
    play_game()
