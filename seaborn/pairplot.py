import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('penguins')
sns.set_style('whitegrid')
# sns.pairplot(data=df,hue='island',palette="Set2",diag_kind="hist")
gr=sns.PairGrid(data=df,hue='species',palette="Set2")
gr.map_upper(sns.scatterplot)
gr.map_lower(sns.histplot)
gr.map_diag(sns.kdeplot)
gr.add_legend()
plt.show()