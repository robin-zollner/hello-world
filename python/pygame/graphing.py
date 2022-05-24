from matplotlib import pyplot as plt
import numpy as np

def vert(val=10, lim=10):
    x = np.ones(lim)*val
    y = np.linspace(1, lim, lim)
    return x,y


def line(m=1, b=0, lim=10):
    x = np.linspace(1, lim, lim)
    y = np.zeros(len(x))

    for i in range(len(x)):
        y[i]+= m*x[i] + b
    return x,y

m = 1
b = 0
lim = 3
val = 3
a,b = line(m, b, lim)
p,q = vert(val, lim)

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
figframe = tk.Frame(root).pack(side=tk.TOP)
uiframe = tk.Frame(root).pack(side=tk.TOP, fill=tk.BOTH)

# UI Elements
quit = tk.Button(uiframe, text="Quit", command=root.quit).pack(side=tk.TOP)
l1 = tk.Label(uiframe, text="Graphing the linear equations:\n y = {} x + {} \n y = {}".format(m, b, val)).pack(side=tk.TOP)

root.title("Graphing")

fig = plt.figure()

lin = FigureCanvasTkAgg(fig, figframe)
lin.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

plt.plot(a,b)
plt.plot(p, q)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Graph")
format(100)

root.mainloop()