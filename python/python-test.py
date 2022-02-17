print("hello world")
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,1,11)
y = x  * x

plt.plot(x,y)
