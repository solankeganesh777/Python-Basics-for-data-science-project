# Normal/Gaussian distribution

x=random.normal(loc=1,scale=2,size=(5))
print(x)

sns.distplot(random.normal(loc=1,scale=2,size=(5)))
#sns.distplot(random.normal(loc=2,scale=0.5,size=10), hist=False)
plt.show()
