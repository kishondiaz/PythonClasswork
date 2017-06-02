# Kishon Diaz
#project2.py

from graphics import *
from time import *


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
gTextMessage = Text(gPointCenterText, "")
gTextP1Count = Text(gPointP1Counter, "")
gTextP2Count = Text(gPointP2Counter, "")
gTextTieCount = Text(gPointTie, "")
gRules = (" The rules of Rock, Paper, Sissors are as followed:\n"+
          "scissors beats paper,\n"+
          "paper beats rock\n"+
          "rock beats scissors")
gIntroMessage = ("** Click a Weapon Below**\n "+
		 "  Player 1")

    


def showMessage(message):
    gTextMessage.undraw()
    gTextMessage.setText(message)
    gTextMessage.setSize(15)
    gTextMessage.draw(gWin)    
    return
def graphDispay():
    showRectangle(gPointQuit, 1.5, 0.75, "red")
    tmp = Text(gPointQuit, "Quit")
    tmp.setSize(18)
    tmp.draw(gWin)

    showRectangle(gPointTitle, 3.5,0.75,"white")
    tTitle = Text(gPointTitle, "Rock Paper Scissors")
    tTitle.setSize(18)
    tTitle.draw(gWin)
    
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

    
    showRectangle(gPointRule, 1.5, 0.75, "green")
    tRule = Text(gPointRule, "Rules")
    tRule.setSize(16)
    tRule.draw(gWin)

    showRectangle(gPointDShadow, 5.5, 2.3, "gray30")

    showRectangle(gPointBackColor, 6, 1.9,"DeepSkyBlue4" )
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

    
def chooseNumPlayers():
    validChoices = [1,2]
    choice = 0
    if choice in validChoices:
        return choice
    return choice
            

def chooseWeapon(numberPlayers):
    p1 = gWin.getMouse()
    if clickedButton(p1, gPointQuit, 1, 1):
        return 0
    while True:
        weapon = 0
        if clickedButton(p1, gPointQuit, 2, 2):
            break
        elif clickedButton(p1,gPointRule, 2,2 ):
            showMessage(gRules)
            break
        elif clickedButton(p1, gPointRock, 1.5, 1.5):
            print("You clicked the Rock image")
            weapon = 1
            return weapon
        elif clickedButton(p1, gPointPaper, 1.5, 1.5):
            print("You clicked the Paper image")
            weapon = 2
            return weapon
        elif clickedButton(p1, gPointScissor, 1.5, 1.5):
            print("You clicked the Scissor image")
            weapon = 3
            return weapon

            
    return weapon

def playGame(numPlayers):
    p1 = gWin.getMouse()
    player1WinCount = 0
    player2WinCount = 0
    player1Results = ""
    player2Results = ""
    player1Weapon = 0
    player2Weapon = 0
    tiedResults = 0
    rockBeatscissors = 0
    weapons = ["","Rock","Paper", "Scissors"]
    

    while True:
        if clickedButton(p1, gPointQuit, 1, 1):
            return 0
        showMessage("Player 1 Turn")
        player1Weapon = chooseWeapon(numPlayers)
        print("player 1 turn")
        player1Results = weapons[player1Weapon]
        showMessage("Player 1 Choose {0}".format(player1Results))
        sleep(.5)



        if clickedButton(p1, gPointQuit, 1, 1):
            return 0 
        if numPlayers == 1:
            if clickedButton(p1, gPointQuit, 1, 1):
                return 0
            showMessage("Player 2 Turn")
            player2Weapon = chooseWeapon(numPlayers)
            print("player 2 turn")
            player2Results = weapons[player2Weapon]
            showMessage("Player 2 Choose {0}".format(player2Results))
            sleep(.5)

        if player1Weapon == clickedButton(p1, gPointQuit, 1, 1):
            break
        elif player1Weapon == player2Weapon:
            tiedResults += 1
            gTextTieCount.undraw()
            gTextTieCount.setText("Tied: {0}".format(tiedResults))
            gTextTieCount.setSize(15)
            gTextTieCount.draw(gWin)
            showMessage("Tie")
        elif player1Weapon == 1 and player2Weapon == 3 :
            player1WinCount += 1
            gTextP1Count.undraw()
            gTextP1Count.setText("Player1 Score: {0}".format(player1WinCount))
            gTextP1Count.setSize(15)
            gTextP1Count.draw(gWin)
            showMessage("Player 1 WON")
        elif player2Weapon == 1 and player1Weapon == 3 :
            player2WinCount += 1
            gTextP2Count.undraw()
            gTextP2Count.setText("Player2 Score: {0}".format(player2WinCount))
            gTextP2Count.setSize(15)
            gTextP2Count.draw(gWin)
            showMessage("Player 2 WON") 
            
        elif player1Weapon > player2Weapon:
            player1WinCount += 1
            gTextP1Count.undraw()
            gTextP1Count.setText("Player1 Score: {0}".format(player1WinCount))
            gTextP1Count.setSize(15)
            gTextP1Count.draw(gWin)
            showMessage("Player 1 WON")
        else:
            player2WinCount += 1
            gTextP2Count.undraw()
            gTextP2Count.setText("Player2 Score: {0}".format(player2WinCount))
            gTextP2Count.setSize(15)
            gTextP2Count.draw(gWin)
            showMessage("Player 2 WON")
        sleep(.9)
        sys.stdout.flush()

            
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
    
    graphDispay()
##
##    for i in range(1, 6):
##        Line(Point(i, 0), Point(i, 6)).draw(gWin)
##    for i in range(1, 6):
##        Line(Point(0, i), Point(6, i)).draw(gWin)

    while True:
        p1 = gWin.getMouse()
        if clickedButton(p1, gPointQuit, 1, 1):
            break
        elif clickedButton(p1,gPointRule, 1.5,1.5 ):
            showMessage(gRules)
        else:
            playGame(1)

    
    

 

    gWin.close()


    
main()

    

    
    
    
    
