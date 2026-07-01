import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1. Load Data
iris = datasets.load_iris()

# Select only ONE feature (Petal Width) so we can plot a clean 2D curve
x = iris['data'][:, 3:] 
y = (iris['target'] == 2).astype(np.int64)

# 2. Split Data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# 3. Scale Data (Fixed data leakage)
ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)  # Use .transform() here!

# 4. Train Model
model = linear_model.LogisticRegression()
model.fit(x_train, y_train)

# 5. Evaluate
y_predicted = model.predict(x_test)
print(f"Accuracy: {model.score(x_test, y_test) * 100:.2f}%")

# 6. Plotting the Logistic S-Curve
# Sort the test data so the line plot connects sequentially rather than jumping around
sort_idx = np.argsort(x_test.flatten())
x_test_sorted = x_test[sort_idx]

y_proba = model.predict_proba(x_test_sorted)

plt.figure(figsize=(8, 5))
plt.scatter(x_test, y_test, color='red', label='Actual Data')
plt.plot(x_test_sorted, y_proba[:, 1], color='blue', linewidth=2, label='Probability of Virginica')
plt.xlabel('Scaled Petal Width')
plt.ylabel('Probability / Class')
plt.title('Logistic Regression Probabilities')
plt.legend()
plt.grid(True)
plt.show()