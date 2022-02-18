"""
This is a test document, to see if I can integrate my GitHub with my local compiler.
Another goal is to see if I can successfully make matplotlib charts here.
"""
import numpy as np
# Import Statements
from matplotlib import pyplot as plt

print("hello world")

x = np.linspace(0, 1, 11)
y = x * x

fig = plt.figure()
plt.plot(x, y)
fig.show()

print(x)
print(y)
