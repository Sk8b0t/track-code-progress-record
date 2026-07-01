import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=sns.load_dataset('penguins')
sns.set_style('darkgrid')
print(df)
# sns.barplot(data=df,x="species",y="body_mass_g",hue='sex',palette=['yellow','green'],estimator=np.std)
sns.countplot(data=df,x='island',hue='sex',palette=['yellow','black'])
plt.show()