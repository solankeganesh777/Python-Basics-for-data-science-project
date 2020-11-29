# Matplotlib Plotting

#Plotting X and Y points
x=np.array([1,4,5,7])
y=np.array([5,3,9,5])
plt.plot(x,y)
plt.show()

print("\n")
#Plotting without line
x=np.array([1,4,5,7])
y=np.array([5,3,9,5])
plt.plot(x,y,'o')
plt.show()

print("\n")
# Multiple points
x=np.array([1,6,4,2,5,7])
y=np.array([5,3,8,9,3,5])
plt.plot(x,y)
plt.show()

print("\n")
# Default X points: here it takes xpoints defaultly as [0,1,2...]
y=np.array([5,3,9,5])
plt.plot(y)
plt.show()
