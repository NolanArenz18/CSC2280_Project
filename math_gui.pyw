from graphics import *


def main():
    # Create graphics window
    win = GraphWin(title="f(x,y)", width=300, height=240)
    #***Add/modify code here**
    win.setBackground(color_rgb(204,236,255))
    # Add text objects
    xtext = Text(Point(80,30), "x")
    xtext.setSize(18)
    xtext.draw(win)

    ytext = Text(Point(80,55), "y")
    ytext.setSize(18)
    ytext.draw(win)
    #***Add/modify code here**

    ftext = Text(Point(60,90), "f(x,y)")
    ftext.setSize(18)
    ftext.draw(win)

    outputtext = Text(Point(150,140), "x + y = 3")
    outputtext.setSize(18)
    outputtext.setStyle("italic")
    outputtext.setTextColor("red")
    outputtext.draw(win)
    #***Add/modify code here**

    # Add entry objects
    xentry = Entry(Point(170,30), 15)
    xentry.setFill("white")
    xentry.setText("1.0")
    xentry.draw(win)

    yentry = Entry(Point(170,60), 15)
    yentry.setFill("white")
    yentry.setText("2.0")
    yentry.draw(win)

    fentry = Entry(Point(170, 90), 15)
    fentry.setFill("white")
    fentry.setText("x + y")
    fentry.draw(win)
    #***Add/modify code here**

    # Add button object
    #***Add/modify code here**
    rect = Rectangle(Point(110, 190), Point(210, 220))
    rect.setFill(color_rgb(100, 100, 255))
    rect.draw(win)

    text = Text(Point(160, 205), "OK")
    text.setSize(20)
    text.draw(win)

    # As long as the window is open, allow multiple computations
    while True:
        # Wait for user input
        #***Add/modify code here**
        win.getMouse()
        # Extract inputs
        #***Add/modify code here**
        y = float(yentry.getText())
        x = float(xentry.getText())
        f = fentry.getText()

        # Evaluate the function using the two inputs
        z = eval(f)

        # Update the output text
        #***Add/modify code here**
        a = " = "

        outputtext.setText(str(f) + str(a) + str(z))
        outputtext.setTextColor("red")
        outputtext.setStyle("italic")

        win.getMouse()
        win.Close()

main()
