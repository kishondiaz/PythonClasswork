# Author: Kishon Diaz
# Date: 02/7/2014
# File: volume_and_surface.py
# Description: This is a program to calculate the volume and surface area of a sphere

"""
ALGORITHM:  The pseudocode description for how the program performs its tasks.
Write as many lines as necessary in this space to describe the
method selected to solve the problem at hand.

1. Print a welcome statement.
2. Ask the user to input their name.
3. Call the greet() function to update the visitor count and print
   a statement to greet the user.
4. Print an exit statement.
5. End the program
"""

# IMPORT STATEMENTS
import math
# GLOBAL VARIABLES
message = "Please enter a number or Q to quit, R to restart\n"
errorMessage = "Please Follow the prompt or Q to quit, R to restart\n"
rightAnswer = "Program will now start over\n"

# FUNCTIONS
def oper():
    print("This is a program to calculate the volume and surface area of a sphere \n")
    choice=input("Enter A for Area or V for Volume and Q to quit: ")

    if choice == "A"or choice == "a":
        area()
    elif choice == "V" or choice == "v":
        volume()
    elif choice =="q" or choice == "Q":
        end()
    else:
        if(choice != correctinput):
            if choice != "A" or choice != "a":
                correctinput()
            elif choice != "V" or choice != "v":
                correctinput()
    if(choice != "Q" or choice != "q"):
        repeat()
    elif (choice == "Q" or choice == "q"):
        end()

def volume():
    rad = input("Enter a number value for the volume: ")
    #x = eval(rad)
    #vol = 4/3*math.pi*x**3
    #print("The Volume of the Sphere is: ",vol)
    while True:
        if rad == "":
            print(message)
            #return 0
            return volume()
        elif rad == "q" or rad == "Q":
            end()
        elif rad == "r" or rad == "R":
            oper()
        try:
            n = float(rad)
            if n < 1:
                print(message)
                return volume()
            elif n > 1:
                rad = float(rad)
                vol = 4/3*math.pi*rad**3
                print(vol)
                print(rightAnswer)
                oper()
            else:
                break
        except ValueError:
            #Well i tried == to catch the ValueError but for some reason != seems to work
            #Please explain i cant figure it out is it something to do with ValueError
            value = rad
            if(value != ""):
                print(errorMessage)
                return volume()
            elif(value != ValueError):
                return volume()
            
    #return n
    
 
    
def area():
    rad = input("Enter a number value for the area:  ")
    #thisArea = 4*math.pi*rad**2
    #print("The Area of the Sphere is: ", thisArea)
    while True:
        if rad == "":
            print(message)
            return area()
        elif rad == "q" or rad == "Q":
            end()
        elif rad == "r" or rad == "R":
            oper()
        try:
            n = int(rad)
            if n < 1:
                print(message)
                return area()
            elif n > 1:
                rad = int(rad)
                thisArea = 4*math.pi*rad**2
                print(thisArea)
                print(rightAnswer)
                oper()
            else:
                break
        except ValueError:
            #Well i tried == to catch the ValueError but for some reason != seems to work
            #Please explain I cant figure it out is it something to do with ValueError
            value = rad
            if(value != ""):
                print(errorMessage)
                return area()
            elif(value != ValueError):
                return area()
        

def end():
    cont = input("Are you sure you want to quit yes or No press Y or N: \n")
    #ending = quit(input("The program has ended"))
    #quitting = ending
    if cont == "n" or cont == "N":
        oper()
    elif cont == "y" or  cont == "Y":
        ending = quit(input("The program has ended \n"))
        end()
        exit
    #else:
        #ending = quit(input("The program has ended"))
        #end()
        #exit()

def correctinput():
     print("Please choose from the prompt! \n")

def repeat():
    while True:
        oper()


# MAIN FUNCTION
def main():
    oper()

main()
