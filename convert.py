# Author: Kishon Diaz
# Date: 02/2/2014
# File: convert.py
# Description: A prgram to convert Celsius temps to Fahrenheit


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

# FUNCTIONS

# MAIN FUNCTION
def main():
    #celsius = eval(input("What is the Celsius temperature? "))
    celsius = 0
    #fahrenheit = 9/5 * celsius + 32 
    #print("The temperature is", fahrenheit, "degrees Fahrenheit. ")

    for i in range(0,101,10): 
        celsius = i
        fahrenheit = int((9/5 * celsius + 32))
        print("The temperature is",i,"in dregress Celsius", "degrees Fahrenheit", fahrenheit,".")
        
        
        
main()
