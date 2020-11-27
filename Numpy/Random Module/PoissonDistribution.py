# poisson distribution

x=random.poisson(lam=2,size=10)
print(x)

sns.distplot(random.poisson(lam=2,size=10),kde=False)
plt.show()
