
def cube(n):
    print( [i ** 2 for i in n])

cube([8, 9, 11])


def listsum(x):
    zed = sum(x)
    print(zed)

listsum([4, 5, 10])


def grade(score):
    if score < 60.0:
        print("F")
    if 60.0<=score<70.0:
        print("D")
    if 70.0<=score<80.0:
        print("C")
    if 80.0<=score<90.0:
        print("B")
    if score>=90.0:
        print("A")
grade(60)


def isleapyear(year):

    if year%4==0:
        if year%400==0:
            print(1)
        if year%100==0:
            if year%400!=0:
                print(0)
        if year%100!=0:
            print(1)
    if year%4!=0:
        print(0)

isleapyear(1600)

from graphics import *
def bounce():
    dx = 1
    dy = 1
    win = GraphWin("Bounce",400,400)
    center = Point(dx, dy)
    circ = Circle(center, 10)
    circ.setFill('blue')
    circ.draw(win)

    for i in range(1000):
        if dx <= 390:
            dx = dx + 1
        if dx >=390:
            dx = dx -1
        dy = dy + 1
        circ.move(dx,dy)
        update(10)
    win.getKey()
    win.close()
bounce()
# I feel very close on this last one I just cant figure out how to
# Set up the if statements so that it will go back all the way and bounce properly
