# Matplotlib Pie Charts

x=np.array([10,25,45,20])
my_lables=np.array(["Ganesh","Mangesh","sid","shub"])
plt.pie(x)
plt.show()

# Labelling
plt.pie(x,labels=my_lables)
plt.show()

#StartAngle
plt.pie(x,labels=my_lables,startangle=90)
plt.show()

#Explode
my_explode=[0.2,0,0,0]
plt.pie(x,labels=my_lables,startangle=90,explode=my_explode)
plt.show()

#Shadow
plt.pie(x,labels=my_lables,startangle=90,explode=my_explode,shadow=True)
plt.show()

#Colors
colors=['c','m','y','k']
plt.pie(x,labels=my_lables,startangle=90,explode=my_explode,shadow=True,colors=colors)
plt.show()

# Legend
plt.pie(x,labels=my_lables,startangle=90,explode=my_explode,shadow=True,colors=colors)
plt.legend(title="Guys Choices")
plt.show()
