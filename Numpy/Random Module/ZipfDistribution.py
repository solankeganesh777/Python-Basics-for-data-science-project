# Zipf distribution

x-random.zipf(a=2,size=(2,3))
print(x)

x=random.zipf(a=2,size=1000)
sns.distplot((x[x<10]),kde=False)
plt.show()
