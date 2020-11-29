# Matplotlib subplots

x=np.array([1,2,3,4])
y=np.array([5,6,7,8])

plt.subplot(1,2,1)
plt.plot(x,y,'*--r',mec='g',mfc='b',ms=15,ls='-.',lw=5,c='y')

x=np.array([8,7,6,5])
y=np.array([4,3,2,1])

plt.subplot(1,2,2)
plt.plot(x,y,'D:c',mec='m',mfc='y',ms=20,ls=':',lw='2',c='k')

plt.show()
