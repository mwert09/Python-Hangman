# A simple hangman game
# TODO: Add multiplayer support
# TODO: Get random words from the internet

import random
import art
import word_list
from os import system

# Display 
def printDisplay():
    print(f"{' '.join(display)}")
    print(art.stages[lives])

def checkLetters():
    count = 0
    for i in range(len(display)):
        letter = display[i]
        if letter == guess:
            print("You've already guessed this letter")
            input("Press any button to continue")
            return
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
            count += 1
    if count == 0:
        global lives
        lives -= 1
        print(f"{guess} is not in the word")
        input("Press any button to continue")

def checkEndGame():
    if '_' not in display:
        print("You Win!")
        return True
    if lives <= 0:
        print("You Lost!")
        print(f"Choosen word was {chosen_word}")
        return True

def Start():
    print(f"{' '.join(display)}")
    print(art.stages[lives])
    print(display)

def Restart():
    global end_game
    global lives
    global chosen_word
    global display
    chosen_word = random.choice(word_list.word_list)
    display = []
    for letter in range(len(chosen_word)):
        display += "_"
    end_game = False
    lives = 6

def CheckReplay():
    replay = input("Do you want to play again? (Y/N - yes/no)").lower()
    if replay == 'y' or replay == "yes":
        Restart()
        system('cls')
        return True
    elif replay == 'n' or replay == "no":
        system('cls')
        return False
    else:
        print("Invalid answer - Exiting...")

player_wants_to_play = True
display = []
lives = 6
end_game = False

#Print Logo
print(art.logo)

# Get a random word from the word list
chosen_word = random.choice(word_list.word_list)
#print(art.stages[lives])

for letter in range(len(chosen_word)):
    display += "_"
#print(display)

while player_wants_to_play:
    Start()
    while not end_game:
        #Get user input
        guess = input("Please enter your guess\n").lower()
        checkLetters()
        system('cls')
        printDisplay()
        end_game = checkEndGame()
    
    player_wants_to_play = CheckReplay()


        

