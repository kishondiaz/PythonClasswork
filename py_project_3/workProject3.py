#Kishon Diaz
#workProject.py


from graphics import *
from time import *
import random


gWin = GraphWin("Rock Paper Sissors", 600,600)
gWin.setCoords(0.0, 0.0, 6.0, 6.0)
gWin.setBackground("SteelBlue2")


gPointQuit = Point(5.5,5.6)
gPointCenterText = Point(3,4)
gPointDisplay = Point(3,4)
gPointDShadow = Point(3.2,4)
gPointTitle = Point(3,5.6)
gPointBackColor = Point(3,1.9)
gPointRule = Point(0.75,5.6)
gPointRock = Point(1,2)
gPointPaper = Point(3,2)
gPointScissor = Point(5,2)
gPointP1Counter = Point(1,0.5)
gPointTie = Point(3,0.5)
gPointP2Counter = Point(5,0.5)
gTitleText = Text(gPointTitle, "Rock Paper Scissors")
gTextMessage = Text(gPointCenterText, "")
gTextP1Count = Text(gPointP1Counter, "")
gTextP2Count = Text(gPointP2Counter, "")
gTextTieCount = Text(gPointTie, "")
gRules = (" The rules of Rock, Paper, Sissors are as followed:\n"+
          "scissors beats paper,\n"+
          "paper beats rock\n"+
          "rock beats scissors")
gIntroMessage = ("** Click Here To Start**")
gP1Color = "navy"
gP2Color = "VioletRed4"
gTieColor = "orange red"
gFinalScore = 5
    


def showMessage(message):
    gTextMessage.undraw()
    gTextMessage.setTextColor("Black")
    gTextMessage.setText(message)
    gTextMessage.setSize(15)
    gTextMessage.draw(gWin)    
    return

def winningMessage(message, textColor):
##    print(textColor)
    gTextMessage.undraw()
    gTextMessage.setTextColor(textColor)
    gTextMessage.setText(message)
    gTextMessage.setSize(15)
    gTextMessage.draw(gWin)
    sleep(.5)
    gTextMessage.undraw()
    return
def winningFlashingScreen(message):
    flash = 3
    amount = 0
    while amount < flash:
        showRectangle(gPointDisplay, 5.5,2.2, gP1Color)
        winningMessage(message, gP2Color)
        sleep(0.5)
        showRectangle(gPointDisplay, 5.5,2.2, gP2Color)
        winningMessage(message, gTieColor)
        sleep(0.5)
        showRectangle(gPointDisplay, 5.5,2.2, gTieColor)
        winningMessage(message, gP1Color)
        sleep(0.5)
        winningMessage(message, gP1Color)
        amount = amount + 1
        showMessage("CLICK ANYWHERE TO END")
    
def graphDispay():
    showRectangle(gPointQuit, 1.5, 0.75, "red")
    tmp = Text(gPointQuit, "Quit")
    tmp.setSize(18)
    tmp.draw(gWin)

    showRectangle(gPointTitle, 3.5,0.75,"white")
    gTitleText.setSize(18)
    gTitleText.draw(gWin)
    
    showRectangle(gPointP1Counter,2.5,1,"DarkSeaGreen2")
    gTextP1Count.setText("Player1 Score: {0}".format(0))
    gTextP1Count.setSize(15)
    gTextP1Count.setStyle("bold")
    gTextP1Count.setFace("times roman")
    gTextP1Count.draw(gWin)
    
    showRectangle(gPointP2Counter,2.5,1,"DarkSeaGreen2")
    gTextP2Count.setText("Player2 Score: {0}".format(0))
    gTextP2Count.setSize(15)
    gTextP2Count.setStyle("bold")
    gTextP2Count.draw(gWin)

    showRectangle(gPointTie,1.6,1,"DarkSeaGreen2")
    gTextTieCount.setText("Tied: {0}".format(0))
    gTextTieCount.setSize(15)
    gTextTieCount.setStyle("bold")
    gTextTieCount.draw(gWin)

    
    showRectangle(gPointRule, 1.5, 0.75, "light sea green")
    tRule = Text(gPointRule, "Rules")
    tRule.setSize(16)
    tRule.draw(gWin)

    showRectangle(gPointDShadow, 5.5, 2.3, "gray30")

    showRectangle(gPointBackColor, 6, 1.9,"DeepSkyBlue4" )
    
    showRectangle(Point(1.1,2.05), 1.5, 1.5, "gray30")
    showRectangle(Point(3.1,2.05), 1.5, 1.5, "gray30")
    showRectangle(Point(5.1,2.05), 1.5, 1.5, "gray30")
    Image(gPointRock, "rock.gif").draw(gWin)
    showRectangle(gPointRock, 1.5, 1.5, "")
    Image(gPointPaper,"paper.gif").draw(gWin)
    showRectangle(gPointPaper, 1.5,1.5, "")
    Image(gPointScissor,"scissors.gif").draw(gWin)
    showRectangle(gPointScissor, 1.5,1.5,"")

    showRectangle(gPointDisplay, 5.5,2.2, "honeydew2")
    gTextMessage.setText(gIntroMessage)
    gTextMessage.setSize(18)
    gTextMessage.draw(gWin)

    

            

def chooseWeapon(numPlayers , whichPlayer):
    validChoices = [1,2,3]
    while True:
        choice = 0
        p1 = gWin.getMouse()
    
        if clickedButton(p1, gPointQuit, 1, 1):
            break
        elif clickedButton(p1,gPointRule, 1,1 ):
            showMessage(gRules)
            break
        elif clickedButton(p1, gPointRock, 1.5, 1.5):
            print("You clicked the Rock image")
            showRectangle(gPointRock, 1.5, 1.5, "white")
            sleep(.3)
            showRectangle(gPointRock, 1.5, 1.5, "")
            Image(gPointRock, "rock.gif").draw(gWin)
            choice = 1
            return choice
        elif clickedButton(p1, gPointPaper, 1.5, 1.5):
            showRectangle(gPointPaper, 1.5, 1.5, "white")
            sleep(.3)
            showRectangle(gPointPaper, 1.5, 1.5, "")
            Image(gPointPaper,"paper.gif").draw(gWin)
            print("You clicked the Paper image")
            choice = 2
            return choice
        elif clickedButton(p1, gPointScissor, 1.5, 1.5):
            showRectangle(gPointScissor, 1.5, 1.5, "white")
            sleep(.3)
            showRectangle(gPointScissor, 1.5, 1.5, "")
            Image(gPointScissor,"scissors.gif").draw(gWin)
            print("You clicked the Scissor image")
            choice = 3
            return choice

            
    return choice

def playGame(numPlayers, p1):
##    p1 = gWin.getMouse()
    player1WinCount = 0
    player2WinCount = 0
    player1Results = ""
    player2Results = ""
    player1Weapon = 0
    player2Weapon = 0
    tiedResults = 0
    rockBeatscissors = 0
    weapons = ["","Rock","Paper", "Scissors"]
    if clickedButton(p1, gPointQuit, 1, 1):
        return 0

    while True:
            if clickedButton(p1, gPointQuit, 1, 1):
                break
            print("player 1")
            showMessage("Player 1 Turn")
            player1Weapon = chooseWeapon(numPlayers, 1)
            player1Results = weapons[player1Weapon]
            showMessage("Player 1 Choose {0}".format(player1Results))
            sleep(.5)
            sys.stdout.flush()
            if player1Weapon == 0:
                break
            if numPlayers == 1:
                print("player 2")
                showMessage("Player 2 Turn")
                player2Weapon = chooseWeapon(numPlayers, 2)
                player2Results = weapons[player2Weapon]
                showMessage("Player 2 Choose {0}".format(player2Results))
                sleep(.5)
                sys.stdout.flush()
                if player2Weapon == 0:
                    break
            if player1Weapon == player2Weapon:
                tiedResults += 1
                gTextTieCount.undraw()
                gTextTieCount.setTextColor(gTieColor)
                gTextTieCount.setText("Tied: {0}".format(tiedResults))
                gTextTieCount.setSize(15)
                gTextTieCount.draw(gWin)
                showMessage("Tie")
##                winningMessage("Tie", gTieColor)
            elif player1Weapon == 1 and player2Weapon == 3 :
                player1WinCount += 1
                gTextP1Count.undraw()
                gTextP1Count.setTextColor(gP1Color)
                gTextP1Count.setText("Player1 Score: {0}".format(player1WinCount))
                gTextP1Count.setSize(15)
                gTextP1Count.draw(gWin)
                showMessage("Player 1 WON")
##                winningMessage("Player 1 WON", gP1Color)
            elif player2Weapon == 1 and player1Weapon == 3 :
                player2WinCount += 1
                gTextP2Count.undraw()
                gTextP2Count.setTextColor(gP2Color)
                gTextP2Count.setText("Player2 Score: {0}".format(player2WinCount))
                gTextP2Count.setSize(15)
                gTextP2Count.draw(gWin)
                showMessage("Player 2 WON")
##                winningMessage("Player 2 WON", gP2Color)
            
            elif player1Weapon > player2Weapon:
                player1WinCount += 1
                gTextP1Count.undraw()
                gTextP1Count.setTextColor(gP1Color)
                gTextP1Count.setText("Player1 Score: {0}".format(player1WinCount))
                gTextP1Count.setSize(15)
                gTextP1Count.draw(gWin)
                showMessage("Player 1 WON")
##                winningMessage("Player 1 WON", gP1Color)
                
            else:
                player2WinCount += 1
                gTextP2Count.undraw()
                gTextP2Count.setTextColor(gP2Color)
                gTextP2Count.setText("Player2 Score: {0}".format(player2WinCount))
                gTextP2Count.setSize(15)
                gTextP2Count.draw(gWin)
                showMessage("Player 2 WON")
##                winningMessage("Player 2 WON", gP2Color)
            sleep(.5)
            sys.stdout.flush()
            if tiedResults > player1WinCount and tiedResults > player2WinCount:
                gTitleText.undraw()
                showRectangle(gPointDisplay, 5.5,2.2, gTieColor)
                gTitleText.setTextColor(gTieColor)
                gTitleText.draw(gWin)
            elif (player1WinCount > player2WinCount and player1WinCount > tiedResults):
                gTitleText.undraw()
                showRectangle(gPointDisplay, 5.5,2.2, gP1Color)
                gTitleText.setTextColor(gP1Color)
                gTitleText.draw(gWin)
            elif (player2WinCount > player1WinCount and player2WinCount > tiedResults):
                gTitleText.undraw()
                showRectangle(gPointDisplay, 5.5,2.2, gP2Color)
                gTitleText.setTextColor(gP2Color)
                gTitleText.draw(gWin)
            else:
                gWin.flush()
                
            winner(tiedResults,player1WinCount,player2WinCount)
            
def winner(tiedResults,player1WinCount,player2WinCount):
    if tiedResults == gFinalScore :
        winningFlashingScreen("The Game is Tied!")
        p1 = gWin.getMouse()
        showMessage("Game will end")
        sleep(1)
        gWin.close()
    elif player1WinCount == gFinalScore :
        winningFlashingScreen("PLAYER 1 HAS WON THE GAME!!!")
        p1 = gWin.getMouse()
        showMessage("Game will end")
        sleep(1)
        gWin.close()
    elif player2WinCount == gFinalScore :
        winningFlashingScreen("PLAYER 2 HAS WON THE GAME!!!")
        p1 = gWin.getMouse()
        showMessage("Game will end")
        sleep(1)
        gWin.close()
        
        
    return 

            
def showRectangle(anchor, width, height, color):
    x1 = anchor.getX() - (width/ 2.0)
    y1 = anchor.getY() - (height/ 2.0)
    x2 = anchor.getX() +(width/2.0)
    y2 = anchor.getY() + (height/2.0)
    r = Rectangle(Point(x1, y1), Point(x2, y2))
    if color:
        r.setFill(color)
    r.draw(gWin)

def clickedButton(point, center, xSize, ySize):
    val = False
    px = point.getX()
    py = point.getY()
    tmp = center
    x = tmp.getX()
    y = tmp.getY()
    if abs(px - x) < (xSize/ 2.0) and abs(py - y) < (ySize / 2.0):
        val = True
    return val
def main():
    
    # Build the game display
    graphDispay()
##
##    for i in range(1, 6):
##        Line(Point(i, 0), Point(i, 6)).draw(gWin)
##    for i in range(1, 6):
##        Line(Point(0, i), Point(6, i)).draw(gWin)
    validChoices = [1,2]
    choice = 1
    while True:
        p1 = gWin.getMouse()
        if clickedButton(p1, gPointQuit, 1, 1):
            break
        elif clickedButton(p1,gPointRule, 1.5,1.5 ):
            showMessage(gRules)
        else:
            validChoices = [1,2]
            choosing = True
            choice = 1
            while choice < 2:
                # Player 1
                #print("test point", choice)
                playGame(choice, p1)
                break
                choice = choice + 1
                # Player 2
                #print("test point", choice)
                playGame(choice, p1)

   

    
    

 

    gWin.close()

if __name__ == "__main__":
    main()

    

    
    
    
    
