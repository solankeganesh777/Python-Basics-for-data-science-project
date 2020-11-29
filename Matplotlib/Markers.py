# Matplotlib Markers

x=np.array([1,2,3,4])
y=np.array([5,7,6,8])
plt.plot(x,y,marker='o')
plt.show()

plt.plot(x,y,marker='*')
plt.show()

plt.plot(x,y,marker='D')
plt.show()

print("\n")
# Fomat Strings fmt:(marker|line|color)
# Line(solid(-),dotted(:),dashhed(--),Dashed/Dotted(-.))
# Colors(red,green,blue,cyan,magneta,yellow,black,white)
y=np.array([5,1,9,8])
plt.plot(y,'o-k')
plt.show()

print("\n")
#Marker size
y=np.array([5,1,9,8])
plt.plot(y,'o-k',ms=20)
plt.show()

print("\n")
# Marker color: markeredgecolor/mec,markerfacecolor/mfc,
y=np.array([5,1,9,8])
plt.plot(y,'o--k',ms=30,mec='r',mfc='y')
plt.show()
