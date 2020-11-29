# Matplotlib Bar

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['CB Shine','Unicorn','Hornet','CD 110'])
y=np.array([87,125,152,91])
plt.bar(x,y)
plt.show()

# Horizontal bars
plt.barh(x,y)
plt.show()

#Color
plt.bar(x,y,color='y')
plt.show()

# width in bar
plt.bar(x,y,color='m',width=0.5)
plt.show()

# Height in barh
plt.barh(x,y,color='k',height=0.5)
plt.show()
