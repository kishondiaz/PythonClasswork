# Author: Kishon Diaz
# Date: 04/03/2014
# File: myProject2.py

import random
import os

CLEAR = "cls"

def chooseNumPlayers():
    prompt = "--- MAIN MENU---\n"\
             "1) One Player\n"\
             "2) Two Players\n"\
             "Choose game or press Enter to quit: "
    validChoices = ["1","2", ""]

    choosing = True
    while choosing:
        os.system(CLEAR)
        choice = input(prompt)
        if choice in validChoices:
            choosing = False
            if choice == "":
                choice = "0"
        else:
            choice = input("Invalid choice. Press Enter: ")
    return int(choice)

def chooseWeapon(numPlayers, whichPlayer):
    prompt = "--- WEAPON MENU"
    if numPlayers == 2:
        prompt += ": PLAYER" + str(whichPlayer)
    prompt += "--\n"\
              "1) Rock\n"\
              "2) Paper\n"\
              "3) Scissors\n"\
              "Choose weapon or press Enter to return to main menu: "
    validChoices = ["1", "2", "3", ""]
    
    choosing = True
    while choosing:
        os.system(CLEAR)
        choice = input(prompt)
        if choice in validChoices:
            if choice == "":
                choice = 0
                return choice
            elif choice == "1":
                choice = 1
                return choice
            elif choice == "2":
                choice = 2
                return int(choice)
            elif choice == "3":
                choice = 3
                return int(choice)
        else:
            choice = input("Invaild choice. Press ENTER: ")

    return int(choice)
def playGame(numPlayers): 
    player1WinCount = 0
    player2WinCount = 0
    tiedResults = 0
    weapons = ["","Rock", "Paper", "Scissors"]

    while True:
        player1Weapon = chooseWeapon(numPlayers, 1)
        if player1Weapon == 0:
            break
        if numPlayers == 1:
            player2Weapon = random.randrange(0,3)
        elif numPlayers == 2:
            player2Weapon = chooseWeapon(numPlayers, 2)
            if player2Weapon == 0:
                break
        if player1Weapon == player2Weapon:
            print("Its a tie")
            tiedResults += 1
        elif player1Weapon > player2Weapon:
            print("Player 1 Wins")
            player1WinCount += 1
        else:
            print("Player 2 Wins")
            player2WinCount += 1
        player1Results = weapons[player1Weapon]
        player2Results = weapons[player2Weapon]
        print("Player1 Choose:{0} P1Score:{1} | TiedScore:{2}| Player2 Choose:{3} P2Score:{4}"
              .format(player1Results,player1WinCount,tiedResults,player2Results,player2WinCount))
        input("\nPress Enter to continue! ")
        
def main():
    while True:
        numPlayers = chooseNumPlayers()
        if numPlayers == 0: 
            break        
        playGame(numPlayers)


if __name__== "__main__":
    main()
