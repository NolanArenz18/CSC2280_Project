Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This program will be used to make a sudoku puzzle

from graphics import *

# Set relevant parameters
rows = 9 # number of rows in the puzzle
cols = 9 # number of cols in the puzzle
size = 45 # size of each cell, in pixels
margin = 20 # border around the puzzle

win2 = GraphWin(title="Sudoku", width=180, height=180)

win2.setBackground(color_rgb(255, 255, 255))

p1 = Point(10, 10)
p2 = Point(50, 80)
rect = Rectangle(p1, p2)
rect.setWidth(10)
rect.draw(win2)

line = Line(p1, p2)
line.setWidth(5)
line.setOutline(color_rgb(149, 149, 149))

import time
time.sleep(5)

#I was very lost on this assignment becuase I wasn't able to actively participate in the
# in the lecture because of the problems I had importing Graphics
# I'd like to meet up during your office hours to go over this assignment.
