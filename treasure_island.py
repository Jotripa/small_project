#Greetings
print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to the treasure island!")
print("Let's Start your journey!")
#Conditioning
choice1 = input('Choose your way, type "right", "left", or "forward".').lower()

if choice1 == "right":
    choice2 = input('You\'ve found 2 ships, what will you choose ? type "blue" or "gold" ?').lower()
    if choice2 == "gold":
        choice3 = input('You found 3 spots to dig, x, y, and z. where would you like to dig ? ').lower()
        if choice3 == "z":
            print("YOU'VE FOUND THE TREASURE CONGRATS!!!")
        elif choice3 == "x":
            print("Theres nothing in here!")
        elif choice3 == "y":
            print("You got mud!")
        else:
            print("Your choice is not available on list! Game over...")
    else:
        print("OH NO! YOU'VE GOT KILLED BY ANOTHER PIRATE! Game over...")
elif choice1 == "left":
    print("you've got eaten by lions! Game over...")
else:
    print("You've fell into lava! Game over...")
