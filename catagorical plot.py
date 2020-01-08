import matplotlib.pyplot as plt 

import seaborn as sns 
import numpy as np

tips= sns.load_dataset('tips')
# print (tips)

# Bar plot

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.mean)

# count plot

sns.countplot(x="sex",data=tips)
plt.show()