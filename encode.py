# Author: Kishon Diaz
# Date: 02/10/2014
# File: encode.py
# Description: encode string to Unicode code

"""
ALGORITHM:  
"""

# IMPORT STATEMENTS

# GLOBAL VARIABLES

# FUNCTIONS
def oper():
    startingMes = input("Would you like to in encode a message Y for yes, N for no, Q for quit: ")
    if (startingMes == "Y") or (startingMes == "y"):
        encodeing()
    elif (startingMes == "N") or (startingMes == "n"):
        end()
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
   
def encodeing():
    secrectMes = input("Please enter the message to encode: ")
    enco = []
    save = ""
    
    print("\n Here is your secret code: ")
    for chari in secrectMes:
        stri = ""
        saveto = ""
        x=""
        strNum = ord(chari)
        ento = 2 * strNum + 3
        strien = str(ento)
        print(strien, end = " ")
        enco.append(ento)
        #at this point i want to take the numbers out of the string
        #so i can save them into one variable, but i did not
        #know how so i replaced the hell out of it i dont know.
        saveto= str(enco).replace(",","")
        stri = saveto.replace("[", "")
        #print(saveto)
        #print(stri)

    #print()
    #print(saveto)

        
    print()

    askForSave = input("would you like to Save your secret code! Y:yes, N:no ")
    if askForSave == "Y" or askForSave == "y":
        save = stri.replace("]","")
        print("Now saving your code:")
        savein(save)
    elif askForSave == "N" or askForSave == "n":
        return encodeing()
    elif askForSave ==  "Q" or askForSave == "q":
        end()
    
    repeat()
def savein(save):
    print("Now saveing your secrect code into a File")
    #print(save)
    infile = open("encode.py", "r")
    outFileName = input("what is the name of the file you want to save: ")
    outfile = open(outFileName, "w")
    for line in infile:
        print(save , file=outfile)
        break
        
        #outfile.write(save)
        #print(save)
    
    infile.close()
    outfile.close()
    print("Finshed saving your code")
    print("Now starting Over quit at Prompt")
    #data = infile.read()
    #print(data)
        
def end():
    cont = input("Are you sure you want to quit Y for yes N for no: ")
    if cont ==  "N" or cont == "n":
        oper()
    if cont == "Y" or cont ==  "y":
        ending = quit(input("The program is ending \n"))
        return end()

def repeat():
    while True:
        oper()
def correctinput():
    print("Please choose from the prompt! \n")    
  

# MAIN FUNCTION
def main():
    oper()
   
                
main()
