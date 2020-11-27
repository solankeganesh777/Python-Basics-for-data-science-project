# Uniform distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.uniform(size=(3,2))
print(x)

sns.distplot(random.uniform(size=10),hist=False)
plt.show()
