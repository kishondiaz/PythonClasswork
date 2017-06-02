# Author: Kishon Diaz
# Date: 02/10/2014
# File: decode.py
# Description: encode string to Unicode code

"""
ALGORITHM:  
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS
def oper():
    startingMes = input("Would you like to in dncode a message Y/yes, N/no, "+
                        "Q/quit at anytime: ")
    if (startingMes == "Y") or (startingMes == "y"):
        decodeing()
    elif (startingMes == "N") or (startingMes == "n"):
        oper()
    elif (startingMes == "Q") or (startingMes == "q"):
        end()
    elif startingMes != "Q" or startingMes != "q":
        repeat()    
    else:
        if(startingMes != correctinput):
            if startingMes != "Y" or startingMes != "y":
                correctinput()
            elif startingMes != "N" or startingMes != "n":
                correctinput()
def decodeing():
    askToLoad = input("Would you like to load a code or manually input a "+
                      "code Y/Load and N/Manually or R/Restart: ")
    if askToLoad == "Y" or askToLoad == "y":
        load = askToLoad
        load = openFile(load)
        changeToMes = str(load).replace(",","")
        #print(changeToMes)
        switchToMes = str(changeToMes).replace("[","")
        #print(switchToMes)
        convertToMes = str(switchToMes).replace("]","")
        #print(convertToMes)
        secrectMes = convertToMes  
    elif askToLoad == "N" or askToLoad == "n":
        secrectMes = input("Please enter the message to encode: ")
    elif askToLoad == "R" or askToLoad == "r":
        oper()
    elif askToLoad == "Q" or askToLoad == "q":
        end()

    deco = []
    print("This is your message")
    for changeTo in secrectMes.split():
        encodeNumb = int(changeTo)
        dento = (encodeNumb-3)/2
        deco.append(chr(encodeNumb))
        

        stri = "".join(chr(int(dento)))
        print(stri, end="")
        
    print()
def openFile(load):
    load =[]
    fileName = input("Enter file's Name: ")
    infile = open(fileName, "r")
    for line in infile:
        print("Your code is being processed",line[0:0])

    print()
    for numLine in line.split():
        toLoadThis = int(numLine)
        load.append(toLoadThis)
        
    print()
    print("Your code is being loaded! ")
    return load

    infile.close()
def end():
    cont = input("Are you sure you want to quit Y for yes N for no: ")
    if cont ==  "N" or cont == "n":
        oper()
    if cont == "Y" or cont ==  "y":
        ending = quit(input("The program is ending \n"))

def repeat():
    while True:
        oper()
def correctinput():
    print("Please choose from the prompt! \n") 
    
# MAIN FUNCTION
def main():
    oper()
   #openFile()
        

                
main()
