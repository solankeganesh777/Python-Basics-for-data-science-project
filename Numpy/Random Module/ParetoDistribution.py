# Pareto distribution

x=random.pareto(a=2,size=(2,3))
print(x)

sns.distplot(random.pareto(a=2,size=10),kde=False)
plt.show()
