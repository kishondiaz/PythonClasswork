# Author: Kishon Diaz
# Date: 02/16/2014
# File: futureValuehw4.py
# Description: Brief This is a revised future vaule caluation program
# just the required code for the homework

"""
ALGORITHM:  
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES


# FUNCTIONS
    

# MAIN FUNCTION
def main():
    print("This is a revised future vaule caluation program")
    numValue = float(input("enter in the amount of "+
                           "money you want to invest:$"))
    apr = float(input("Enter in decmials percent of intrest:%"))
    yR = int(input("Enter in the amount of years you want to "+
                   "predict to:"))
    yR = yR +1
    print("Year "," " ," Value")
    for i in range(yR):
        numValue = numValue *(1 + apr)
        rnumVale = round(numValue,2)
        print("Yr:"+ str(i)+"  "+"Total: "+ "${:.2f}".format(rnumVale))

main()
