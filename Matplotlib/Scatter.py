# Matplotlib Scatter


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])  #Age of car
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86]) #Speed of car

plt.scatter(x,y)
plt.show()

#Compare plots

# Day 1 
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])  #Age of car
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86]) #Speed of car
plt.scatter(x,y)

#Day2
p = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
q = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(p,q)
plt.title("Compare plots")
plt.show()

#Set color
plt.scatter(x,y,c='r')
plt.scatter(p,q,c='g')
plt.title("Set color")
plt.show()

#Color each dot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,111,86,103,87,94,78,77,85,86,75])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x,y,c=colors)
plt.title("Color each dot")
plt.show()

# COlorMap & Colorbar
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.colorbar()
plt.title("ColorMap")
plt.show()

#Size of dots
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes= np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 1000])
plt.scatter(x,y,s=sizes,c=colors)
plt.show()

#Alpha: Tranaparency of dots
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes= np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 1000])
plt.scatter(x,y,s=sizes,c=colors,alpha=0.5)
plt.show()

#Combine color size and alpha
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=10*(np.random.randint(100,size=(100)))

plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()
