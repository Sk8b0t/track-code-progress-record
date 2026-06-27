import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1. Load, Split, and Scale
iris = datasets.load_iris()
x = iris['data'][:, 2:]  # 2 features
y = (iris['target'] == 2).astype(np.int64)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

# 2. Train and Predict
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)
y_proba = model.predict_proba(x_test)

# --- THE FIX TO MAKE YOUR GRAPH WORK ---
# Sort by the first feature (x_test[:, 0]) so the line plots smoothly
sort_order = np.argsort(x_test[:, 0])
x_plot = x_test[:, 0][sort_order]
y_plot = y_proba[:, 1][sort_order]

# 3. Simple Plot
plt.plot(x_plot, y_plot, color='black', linewidth=2)
plt.xlabel('Scaled Petal Length')
plt.ylabel('Probability of Virginica')
plt.grid(True)
plt.show()