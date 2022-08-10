#Import Module

import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
from hangman_ascii import logo, stages
print(logo)
print(f"the choosen word is {chosen_word}")
#Making blanks display
display = []
for _ in range(word_length):
    display += "_"
#game condition
game_is_end = False
while not game_is_end:
    guess = input(" Guess a letter : ").lower()
    
    #--------------------------------------------
    if guess in display:
      print(f"you already guessed that letter {guess}")
    #--------------------------------------------
    for position in range(word_length):
        letter = chosen_word[position]
    #--------------------------------------------   
        if letter == guess:
            display[position] = letter
    #--------------------------------------------
    if guess not in chosen_word:
        print(f"you guessed {guess}, theres no word in there. -1 life !")
        lives -= 1
        if lives == 0:
            game_is_end = True
            print("you lose")
    #--------------------------------------------
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_is_end = True
        print("you win")
    #--------------------------------------------
    print(stages[lives])