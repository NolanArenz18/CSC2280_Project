from graphics import *
import time


# Color Grid Project

win = GraphWin("Color Grid")

# The first Column

y = 20
r = 55
for i in range(0, 10):
    rect = Rectangle(Point(0,0), Point(20,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    r = r + 2
    y = y + 20
    time.sleep(0.02)
# Column 2

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(20,0), Point(40,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    r = r + 2
    y = y + 20
    time.sleep(0.02)
# Column 3

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(40,0), Point(60,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 4

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(60,0), Point(80,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 5

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(80,0), Point(100,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 6

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(100,0), Point(120,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 7

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(120,0), Point(140,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 8

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(140,0), Point(160,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 9

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(160,0), Point(180,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)
# Column 10

y = 20
for i in range(0, 10):
    rect = Rectangle(Point(180,0), Point(200,y))
    rect.setFill(color_rgb(0, 0, r))
    rect.setOutline(color_rgb(0, 0, r))
    rect.draw(win)
    y = y + 20
    r = r + 2
    time.sleep(0.02)

win.getKey()
win.close()
