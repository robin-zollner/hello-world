from matplotlib import pyplot as plt
import numpy as np


limit = 100000
def harmonicSums(lim):
	x = np.linspace(1, lim, lim)	
	y = np.array([0])

	for i in range(len(x)):
		s = 1/x[i]
		t = y[i]
		u = s + t
		y = np.append(y, u)
	y = np.delete(y,0)
	return x, y
a,b = harmonicSums(limit)

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
figframe = tk.Frame(root).pack(side=tk.TOP)
uiframe = tk.Frame(root).pack(side=tk.TOP, fill=tk.BOTH)


# adding UI elements
uiElments = tk.Frame(uiframe).pack(side=tk.TOP, fill=tk.BOTH)
quit = tk.Button(uiElments, text="Quit", command=root.quit).pack(side=tk.TOP, fill=tk.X)
l1 = tk.Label(uiElments, text="Calc Limit:").pack(side=tk.TOP, fill=tk.BOTH)
e1 = tk.Entry(uiElments, bd=5, textvariable="StringVar").pack(side=tk.TOP)

fig = plt.figure()
har = FigureCanvasTkAgg(fig, figframe)
har.get_tk_widget().pack(side=tk.LEFT, fil=tk.BOTH)
plt.plot(a,b)
plt.xlabel("Natural number (x)")
plt.ylabel("Sum of the Harmonic Series (y)")
plt.title("Sum of Harmonic Series as function of Natural Numbers from 1 to {}".format(limit))

root.mainloop()