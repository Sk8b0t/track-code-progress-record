import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('penguins')
sns.set_style('darkgrid')
sns.kdeplot(data=df,x='body_mass_g',hue='species',palette=['black','red','blue'],fill=True)
plt.show()
