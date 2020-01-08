import seaborn as sns
import matplotlib.pyplot as plt 

tips=sns.load_dataset('tips')

# distplot using seaborn
sns.distplot(tips['total_bill'], kde=False,bins=30)

#jointplot using seaborn with kind value like by defualt scatter 'scatter', 'reg', 'resid', 'kde', or 'hex'
sns.jointplot(x='total_bill',y='tip',data=tips,kind="reg")


# pairplot using seaborn 
""" pairplot will plot pairwise relationships across an entire dataframe 
(for the numerical columns) and 
supports a color hue argument (for categorical columns). hue='sex',palette='coolwarm', here hue means individual data
"""

sns.pairplot(tips,hue='sex',palette='coolwarm')

"""
rugplot
rugplots are actually a very simple concept,
they just draw a dash mark for every point on a univariate distribution.
"""


sns.rugplot(tips["total_bill"])

#kde


plt.show()