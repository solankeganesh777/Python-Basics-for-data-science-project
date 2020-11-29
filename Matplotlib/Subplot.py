# Matplotlib subplots
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
p=np.array([2,4,6,8])
q=np.array([1,3,5,7])


plt.subplot(1,2,1)
plt.plot(x,y,'*--r',mec='g',mfc='b',ms=15,ls='-.',lw=5,c='y')

x=np.array([8,7,6,5])
y=np.array([4,3,2,1])

plt.subplot(1,2,2)
plt.plot(x,y,'D:c',mec='m',mfc='y',ms=20,ls=':',lw='2',c='k')

plt.show()

print("\n")
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Graph 1")

plt.subplot(2,2,2)
plt.plot(p,q)
plt.title("Graph 2")

plt.subplot(2,2,3)
plt.plot(p,q)
plt.title("Graph 3")

plt.subplot(2,2,4)
plt.plot(x,y)
plt.title("Graph 4")

plt.suptitle("Subplot graphs")
plt.show()
