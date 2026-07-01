import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,datasets

iris=datasets.load_iris()
x=iris['data'][:,3:]
y=(iris['target']==2).astype(int)

model=linear_model.LogisticRegression()
model.fit(x,y)
print(model.predict([[1.0],[2.6]]))

test_val=np.linspace(1,3,1000).reshape(-1,1)
y_prob=model.predict_proba(test_val)
print(test_val)
print(y_prob)
plt.plot(test_val,y_prob[:,1])
plt.show()
