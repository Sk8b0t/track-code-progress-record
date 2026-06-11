import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('penguins')
sns.set_style('whitegrid')
col=df.columns.tolist()[2:6]
sns.heatmap(data=df[col].corr(),annot=True,cmap="Blues")
plt.show()