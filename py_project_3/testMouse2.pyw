# testMouse2.pyw
#
# Demonstrates use of a Python GraphWin object, window size,
# coordinate system, mouse input via getMouse(), drawing
# rectangles, ovals, text objects and images using the
# textbook-provided graphics.py module, and a specialized
# function to determine if a mouse click occurs inside
# a rectangular region around a point.

from graphics import *

# Create a window and set its size
gWin = GraphWin("Test Mouse", 400, 400)
gWin.setCoords(0.0, 0.0, 4.0, 4.0)
gWin.setBackground("peachpuff")

gPointQuit = Point(1,1)
gPointTest = Point(2.5, 2.5)
gPointRock = Point(3, 1)
gTextMessage = Text(gPointTest, "")

# Display a message in a rectangular message area
def showMessage(message):
    gTextMessage.undraw()
    gTextMessage.setText(message)
    gTextMessage.setSize(22)
    gTextMessage.draw(gWin)
    return

# Shows a rectangle of width x height centered on center
#  and (optionally) filled with color
def showRectangle(anchor, width, height, color):
    x1 = anchor.getX() - (width / 2.0)
    y1 = anchor.getY() - (height / 2.0)
    x2 = anchor.getX() + (width / 2.0)
    y2 = anchor.getY() + (height / 2.0)
    #print(x1, y1, x2, y2)
    r = Rectangle(Point(x1, y1), Point(x2, y2))
    if color:
        r.setFill(color)
    r.draw(gWin)

# Returns True if the clicked point is inside the rectangle
#  defined by a center point and x, y dimensions
def clickedButton(point, center, xSize, ySize):
    val = False
    px = point.getX()
    py = point.getY()
    tmp = center
    x = tmp.getX()
    y = tmp.getY()
    #print(px, py, x, y)
    if abs(px - x) < (xSize / 2.0) and abs(py - y) < (ySize / 2.0):
        val = True
    return val


def main():
    showRectangle(gPointQuit, 1, 1, "red")
    tmp = Text(gPointQuit, "QUIT")
    tmp.setSize(18)
    tmp.draw(gWin)
    
    showRectangle(gPointTest, 1.5, 1, "green")
    gTextMessage.setText("TEST")
    gTextMessage.setSize(18)
    gTextMessage.draw(gWin)

    Image(gPointRock, "rock.gif").draw(gWin)
    showRectangle(gPointRock, 1.5, 1.5, "")

    # draw grid
    for i in range(1, 4):
        Line(Point(i,0), Point(i,4)).draw(gWin)
    for i in range(1, 4):
        Line(Point(0, i), Point(4, i)).draw(gWin)

    count = 0
    
    while True:
        # Get a mouse click, exit if the pointer is inside the quit button
        p1 = gWin.getMouse()
        print(p1.getX(), p1.getY())
        if clickedButton(p1, gPointQuit, 1, 1):
            break
        elif clickedButton(p1, gPointTest, 1.5, 1):
            count += 1
            print("Count:", count)
            showMessage(str(count))
        elif clickedButton(p1, gPointRock, 1.5, 1.5):
            print("You clicked the Rock image")
            showMessage("Rock")
        else:
            # Create a cirle where the user clicked and show coordinates
            c1 = Circle(p1, 0.25)
            c1.setFill("cyan")
            c1.draw(gWin)
            t1 = Text(p1, "[{0},{1}]".format(int(p1.getX()), int(p1.getY())))
            t1.setSize(14)
            t1.draw(gWin)
            
    gWin.close()

if __name__ == "__main__":
    main()
