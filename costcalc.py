# Author: Kishon Diaz
# Date: 2/9/2014
# File: costcalc.py
# Description: a very simple program to calculate cost of coffe

"""
I made it exit after the program ran because
everytime main() is called back into the python shell
it just resumed where it left off with the results it last had.
Interms I made a onSaved, onResume and didnt know how to fix it yet
if you want to run the program again F5 or run from script

but i think because i dont know how to call a function into
an error function and i built the error system into the operation
of the running function

i fixed it didnt know that if you an input into a global veriale is would act
like a onSave, onResume know i know
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES
#x = input("Put the number amout of your order amount: ")
#message = "Please put in a number value"


# FUNCTIONS

    
def orders():
    x = input("Put the number amout of your order amount Q to quit: ")
    message = "Please put in a number value"
    pounds = 10.50
    order = x
    if x == "q" or x == "Q":
        end()
    while True:
        if order == "":
            print(message)
            return orders()
            #exit(print("sorry please re-run it again from the script"))
        try:
            n = float(order)
            if n < 1:
                print(message)
                return orders()
                #exit(print("sorry please re-run it again from the script"))
            elif n > 1:
                order = float(order)
                newCost =(pounds + order) * (.86 + 1.50)
                print("Your order at:",int(order),"amount is",round(newCost, 2),"dollars")
                print("The program has ended")
                end()
                break
                #exit(print("sorry please re-run it again from the script"))
            else:
                break
        except ValueError:
            print(message)
            return orders()
            #exit(print("sorry please run it again"))

def end():
    
    cont = input("If you want to quit Y for Yes, N for No: \n")
    if  cont == "n"  or cont == "N":
        orders()
    elif cont == "y" or cont == "Y":
        ending = quit(input("The program has ended \n"))
        end()
        exit
    else:
        if cont != "n" or cont != "N":
            print("Please choose yes or no! ")
            return end()
        
# MAIN FUNCTION
def main():
    orders()

main()
