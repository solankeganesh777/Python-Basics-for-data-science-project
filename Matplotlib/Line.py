# Matplotlib Line

# Linestyle
x=np.array([5,3,7,4])
y=np.array([3,2,1,6])
plt.plot(x,y,linestyle='dotted')
plt.show()

plt.plot(x,y,ls='--')
plt.show()

# Line color: color/c
plt.plot(x,y,ls='-.',color='g')
plt.show()

#Line width: linewidth/lw
plt.plot(x,y,ls='-.',c='b',lw=15)
plt.show()

#Multiple lines
p=np.array([7,3,2,1])
q=np.array([2,3,4,5])
plt.plot(x,y,c='r')
plt.plot(p,q,c='g')
plt.show()

p=np.array([7,3,2,1])
q=np.array([2,3,4,5])
plt.plot(x,y,p,q,c='r')
plt.show()
