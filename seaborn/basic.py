import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

print(sns.get_dataset_names())
df=sns.load_dataset('penguins')
print(df)
sns.set_style('darkgrid') #white, dark,whitegrid,,darkgrid,ticks
sns.scatterplot(data=df,x='flipper_length_mm',y='body_mass_g',hue='species')
sns.despine()
sns.set_context('notebook') # paper, poster

plt.show()