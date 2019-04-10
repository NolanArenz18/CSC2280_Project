from graphics import *
import time


# Color Grid Project

win = GraphWin("Color Grid")

# The first Column

y = 20
r = 55
for i in range(0, 10):
    rect = Rectangle(Point(0,0), Point(y,20))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    r = r + 2
    y = y + 20
    time.sleep(0.02)
# Column 2

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,20), Point(y,40))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    r = r + 2
    y = y + 20
    time.sleep(0.02)
# Column 3

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,40), Point(y,60))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 4

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,60), Point(y, 80))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 5

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,80), Point(y,100))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 6

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,100), Point(y,120))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 7

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,120), Point(y,140))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 8

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,140), Point(y,160))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 9

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,160), Point(y,180))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 10

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(0,180), Point(y,200))
    rect.setFill(color_rgb(r, 0, 0))
    rect.setOutline(color_rgb(r, 0, 0))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)


win.getKey()
win.close()
