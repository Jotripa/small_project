#Import module
import random
#ASCII
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#listing ASCII
images = [rock, paper, scissors]
#Input user's choice
user = int(input("Input your choice, 0 for rock, 1 for paper, 2 for scissors\n"))
if user >= 3 or user < 0:
    print("You inputing invalid number!")
else:
    print(f"You choose: ")
    print(images[user])
    #Input computer's choice
    comp = random.randint(0, 2)
    print("Computer choose: ")
    print(images[comp])
    #if statement
    if user == 0 and comp == 2:
        print("You've win the game! Congrats!")
    elif comp == 0 and user == 2:
        print("You've lose the game!")
    elif user > comp:
        print("You've win the game! Congrats!")
    elif comp > user:
        print("You've lose the game!")
    elif user == comp:
        print("It's a draw!")