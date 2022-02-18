"""
This is a document set up in Sublime.
Purpose is to test Sublime's ability to run python.

This will be merged onto https://github.com/robin-zollner/hello-world.git

I do not know the best way to do so yet.

author: @robin-zollner
"""

#%% Test One 

import numpy as np
import matplotlib
from matplotlib import pyplot as plt


print("Hello World") #This is a check.

x = np.linspace(0, 1, 11)
y = x * x

plt.plot(x, y)
plt.show()

#%% Test Two: Making a simple GUI


import tkinter as tk
from tkinter import *
from tkinter import messagebox
top = tk.Tk()
top.geometry("250x250")
def twoPlusTwo():
	msg = messagebox.showinfo("Hello Python", "2 + 2 = 4")
B = Button(top, text = "2 + 2 = ?", command = twoPlusTwo)
B.place(x = 50, y=50)

#%% Making a more complex UI

root = tk.Tk()

import random as r
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set the width and height of the screen [width, height]
print("Enter des625ired grid size")
grid_size = 25 # This might be replaced. int(input())
pxls = grid_size * 25
size = str(pxls) + "x" + str(pxls)
print(size)
screen = root.geometry(str(pxls))
width = 20
height = 20
margin = 1


top.mainloop()
