# Binomial distribution

x=random.binomial(n=10,p=0.5,size=10)
print(x)

sns.distplot(random.binomial(n=10,p=0.5,size=10),hist=True,kde=False)
plt.show()
