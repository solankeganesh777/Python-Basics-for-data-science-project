# rayleigh distribution

x=random.rayleigh(scale=2,size=(2,3))
print(x)

sns.distplot(random.rayleigh(size=10),hist=False)
plt.show()
