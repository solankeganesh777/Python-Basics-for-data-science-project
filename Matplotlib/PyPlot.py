# Matplotlib Intro

import matplotlib
print(matplotlib.__version__)

# Matplotlib pyplot

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,6])
y=np.array([2,3])

plt.plot(x,y)
plt.show()
