# Author: Kishon Diaz
# Date: 02/07/2014
# File: lightning_counter.py
# Description: Brief description of what this program does

"""
ALGORITHM:  based of of the formula from www.grc.nasa.gov and wikihow.com i used
these formulas to create this program.


psuedocode:  create a program name it lighting_counter
def oper():
    this program will give you a choice to choose miles or distance 

def distFeet():
    this will give the distance measrued in feet
    distance = 1100 * time
    print out distFeet

def distMile():
    this will give the distance measured in miles
    distance = time / 5
    print distMile()

def thisTime():
    this will give a number value to a varibale name it sec
    sec will be used to add for time and called into the equtions of
    disMile and disFeet
    error protection aded here

def repeat():
    this will repeat and call the oper() function infintly until Q or q is press
    when Q/q pressed in the oper()function it will call end()

def end():
    will end the program after Q/q is pressed at anytime it will prompt the user
    if they are sure they want to quit if yes quit and exit program if no return
    to prgram from oper() if nothing is entered and enter is preesed it will return
    where it left off at and resume program.
def correctInput():
    is a prompt for if the user chooses the wrong input in oper()
    
def main():
    will call oper()

main()
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES
message = "Please enter the right time in seconds or Q to quit, R to restart\n"
errorMessage = "Please Follow the prompt or Q to quit, R to restart\n"
getFeet = 1

# FUNCTIONS
def oper():
    print("This is a program to calculate the disatance from a lighting strike. ")
    choice = input("choose your distance miles or feet M or F or Q to quit at anytime: ")
    print("\n")

    if choice == "M" or choice == "m":
        distMile()
    elif choice == "F" or choice == "f":
        distFeet()
    elif choice == "Q" or choice == "q":
        end()
    else:
        if (choice != correctInput):
            if choice  != "M" or choice != "m":
                correctInput()
            elif choice != "F" or choice != "f":
                correctInput()

    if(choice != "Q" or choice != "q"):
        repeat()
    elif (choice == "Q" or choice == "q"):
        end()
def distFeet():
    distance = 1100 * thisTime()
    print("This is your approximate distance from the lightning in Feet: ",distance, "ft away\n")
    print("This program will restart\n")
    
def distMile():
    distance =  thisTime() / 5 
    print("This is your approximate distance from the lightning in Mile: ",distance, "Miles away \n")
    print("This program will restart\n")
    
def goThere():
    x = thisTime()
    x == int
    if x == True:
        distFeet()
        
   
def thisTime():
    sec= input("Enter seconds from sight of flash from lighting to the sound of thunder numbers only: ")
    print("\n")
    
    #sec == 60
    #print("at",sec,"seconds")
    while True:
        if sec == "":
            # test point print("you are here")
            print(message)
            return thisTime()
        elif sec == "q" or sec == "Q":
            end()
        elif sec == "r" or sec == "R":
            oper()
        try:
            n = int(sec)
            if n < 1:
                print(message)
                #testpoint print("well then")
                return thisTime()
            elif n > 1:
                sec = int(sec)
                sec == 60
                print("at",sec,"seconds")
                return sec
                oper()
            else:
                break
        except ValueError:
            value = sec
            if(value != ""):
                #testPoint print("right here")
                print(errorMessage)
                return thisTime()
                
            elif(value == ValueError):
                #testpoint print("this is a problem")
                return thisTime()
            
    #return n
    
    return sec
def repeat():
    while True:
        oper()
def end():
    cont = input("Are you sure you want to quit Yes or No press Y or N: \n")
    if  cont == "n"  or cont == "N":
        oper()
    elif cont == "y" or cont == "Y":
        ending = quit(input("The program has ended \n"))
        end()
        exit
def correctInput():
    print("Please choose from the prompt! \n")
        
# MAIN FUNCTION
def main():
    oper()

main()
