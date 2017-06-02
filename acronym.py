# Author: Kishon Diaz
# Date: 02/17/2014
# File: aycrom.py
# Description: just the basics this is a program to make an aycrom out of 3 words limited
# Error corrections becuase of lack of understand

"""
ALGORITHM:  
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES


# FUNCTIONS
def accryn():
    x = ""
    print("This is a program to make an aycrom out of 3 words")
    into = input("Please enter you 3 word phrase: ")
    #splitThis is a list to split var "into" into a list
    splitThis = []
    #This for loop is to take out the individual words in var "into"
    #and split them into separate new varibales
    if into == "":
        error_E = into
        error(error_E)
        return error_E
    elif into == into[0]:
        print("getting intresting")
    else:
        
        for x in into:
            splitThis = into.split()
            intoThis = splitThis[0]
            intoHere = splitThis[1]
            intoThere = splitThis[2]
        
            #var firstinthis takes out the first letters from the new separated words.
            firstinthis = [str(intoThis[0]),str(intoHere[0]),str(intoThere[0])]
        
            #var fullAccr combines the first leters from var firstinthis then makes
            #those letters capitalised.
            fullAccr = "".join(firstinthis).upper()
            #end loop
            
        
    print("This is you 3 word aycrom",fullAccr)
def error(error_E):
    print("you made it here")
    print(error_E)
    y =(error_E)
    print(y)
    while True:
        if y == "":
            print("true")
            accryn()
        try:
            #does not work will figure it out in time
            n = float(y)
            if n == int:
                print("Use only Characters not numbers")
                return accryn()
                break
        except ValueError:
            print("well i am here")
        except TypeError:
            print("why here")

    

# MAIN FUNCTION
def main():
    accryn()

main()
