from tkinter import font
from tkinter.font import Font
from matplotlib import pyplot as plt
import numpy as np
import time

start = time.time()
def vert(val=10, lim=10):
    num = lim*10 + 1
    x = np.ones(num)*val
    y = np.linspace(0, lim, num)
    return x,y


def line(m=1, b=0, lim=10):
    num = lim*10 + 1
    x = np.linspace(0, lim, num)
    y = np.zeros(len(x))

    for i in range(len(x)):
        y[i]+= m*x[i] + b
    return x,y

def sinTop([p1 => tuple, p2 => tuple, p3 => tuple]):
    l1x2 = (p3[0] - p2[0])**2
    l1y2 = (p3[1] - p2[1])**2


m = 1
o = 0
lim = 1
val = 1
a,b = line(m, o, lim)
p,q = vert(val, lim)

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
figframe = tk.Frame(root).pack(side=tk.TOP)
uiframe = tk.Frame(root).pack(side=tk.TOP, fill=tk.BOTH)

# Defining Font
fontStyle = ("Franklin Gothic Book", 16)
# UI Elements
quit = tk.Button(uiframe, text="Quit", command=root.quit, font=fontStyle).pack(side=tk.TOP)
l1 = tk.Label(uiframe, text="Graphing the linear equations:\n y = {} x + {} \n y = {}".format(m, o, val), font=fontStyle)
l1.pack(side=tk.TOP)
eq = tk.LabelFrame(uiframe).pack(side=tk.TOP)
lm = tk.Label(uiframe, text='y: ', font=fontStyle).pack(side=tk.TOP)
e1 = tk.Entry(uiframe, textvariable='StringVar')
b1 = tk.Entry(uiframe, )

root.title("Graphing")

fig = plt.figure()

lin = FigureCanvasTkAgg(fig, figframe)
lin.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

plt.plot(a,b)
plt.plot(p, q)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Graph")
format(lim)
end = time.time()
root.mainloop()

print(end - start)