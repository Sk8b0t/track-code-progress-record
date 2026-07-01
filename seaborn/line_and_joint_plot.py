import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('penguins')
sns.set_style('whitegrid')
print(df)
# sns.lineplot(data=df,x="body_mass_g",y="bill_depth_mm",hue='sex',style='island')
sns.jointplot(data=df,x='bill_depth_mm',y='body_mass_g',hue='island',kind='kde')

plt.show()