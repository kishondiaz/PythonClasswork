# Author: First Last
# Date: mm/dd/yyyy
# File: nameOfProgram.py
# Description: Brief description of what this program does

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

# GLOBAL VARIABLES
ender = 0
# FUNCTIONS
def oper():
    choice=input("Enter + , - , *, /, q to quit :")
             
    if choice == "+":
        add()
    elif choice == "-":
        sub()
    elif choice == "*":
        mult()
    elif choice =="/":
        div()
    #elif choice == "q ":
        #end()
    else:
        if(choice != correctinput):
            if choice != "+":
                if correctinput == choice:
                    correctinput
                elif choice == "q":
                    end()
                elif choice == "Q":
                    end()
                correctinput()
            elif choice != "-":
                correctinput()
            elif choice != "*":
                correctinput()
            elif choice !="/":
                correctinput()
                
                
    if(choice != "q" or "Q"):
        repeat()
    elif(choice == "q" or "Q"):
        end()
    if(choice == error):
          while True:
            x = getX()
            if x == 0:
                print("Exit.")
                break
            print("The number you entered is: ", x)

    if __name__ == "__main__":
        error()
            
       
    #add=input("+")
    #sub=input("-")
    
    #if(choose in add):
        #print(add)
    #    add()
    #elif(choose in sub):
        #print(sub)
    #    sub()

def add():
     x=eval(input("Enter first number"))
     print("+")
     y=eval(input("Enter the second number"))
     result = x + y
     print(result)

def sub():
     x=eval(input("Enter first number"))
     print("-")
     y=eval(input("Enter the second number"))
     result = x - y
     print(result)
def mult():
     x=eval(input("Enter first number"))
     print("*")
     y=eval(input("Enter the second number"))
     result = x * y
     print(result)
def div():
     x=eval(input("Enter first number"))
     print("/")
     y=eval(input("Enter the second number"))
     result = x / y
     print(result)

def end():
        ending=quit(input("The Calcuator has ended"))
        end()
        exit()
def correctinput():
     print("Please choose from the promt!")

def repeat():
    while True:
        oper()
def Errors():
    errorMessage = "\nInvalid value (Must enter a number >= 1 or press ENTER)\n"
    while True:
        oper() = oper()
        if oper() == "":
            return 0
        try:
            n = int(choice)
            if n < 1:
                print(errorMessage)
            else:
                break
        except ValueError:
            print(errorMessage)
    return n# MAIN FUNCTION
def main():
    oper()
    
main()
