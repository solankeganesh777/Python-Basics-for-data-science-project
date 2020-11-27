# Seaborn module: Needed for plotting distribution plots

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([5,1,3,6,8,5,5,5,5,9])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([5,1,3,6,8,5,5,5,5,9,9],hist=False)
plt.show()
