# Logistic distribution

x=random.logistic(loc=1,scale=2,size=(2,3))
print(x)

sns.distplot(random.logistic(size=10),hist=False)
plt.show()
