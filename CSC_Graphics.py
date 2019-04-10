from graphics import *

win = GraphWin()

lefteye = Circle(Point(80,50), 5)
lefteye.draw(win)
lefteye.setFill('yellow')
lefteye.setoutline('red')

righteye = lefteye.clone()
righteye.move(20, 0)
