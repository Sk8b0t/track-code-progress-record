import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
mnist=fetch_openml('mnist_784')
x,y=mnist['data'],mnist['target']
digit=x.loc[30000]
plt.imshow(digit.to_numpy().reshape(28,28),cmap=matplotlib.cm.binary,interpolation="nearest")
plt.axis("off")
print(y.loc[30000])
plt.show()
