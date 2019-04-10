# screenshot.py
# This module was created to enable image capture of a Graphics Window
# created using the Tkinter-based graphics library that accompanies the 
# following textbook:
#
# J. Zelle, "Python Programming: An Introduction to Computer Science." 
# 3rd ed., Wilsonville, OR: Franklin, Beedle, & Associates, 2016. 
# (ISBN-13: 978-1590282755)
#
# Usage
# =====
# To use this module, simply import it:
#
#   from screenshot import *
#
# Then, whenever you need to capture an image, use the command:
#
#   screenshot(win, filename)
#
# where win is any open Graphics Window (GraphWin object) and filename is a 
# string that identifies the fullpath filename of the output image. PNG is 
# recommended, although other options may be compatible.
#
# Requirements
# ============
# In order to use this module, you must install the Python Imaging Library 
# (PIL). There is a simple fork of PIL that can be installed via pip called 
# pillow. To install pillow, open a command prompt (Windows) or Terminal (Mac)
# and type the following command:
#
#   pip install pillow
#
# To verify the installation, use the command:
#
#   pip list
#
# and manually locate Pillow in the list.

# Copyright 2019 Matthew R. Eicholtz

from PIL import ImageGrab

def screenshot(win, filename):
    # Compute the bounds of the window in terms of screen pixels
    x0 = win.winfo_rootx() + win.winfo_x() + 1
    y0 = win.winfo_rooty() + win.winfo_y() + 1
    x1 = x0 + win.winfo_width() - 1
    y1 = y0 + win.winfo_height() - 1
    
    # Adjust for inconsistent display resolution stored by graphics library
    x0 *= 1.5
    y0 *= 1.5
    x1 *= 1.5
    y1 *= 1.5
    
    # Grab the screenshot and save it to file
    ImageGrab.grab(bbox=(x0, y0, x1, y1)).save(filename)
