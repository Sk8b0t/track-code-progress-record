import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model,datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()
print(iris['feature_names'])

x=iris['data'][:,2:]
y=(iris['target']==2).astype(np.int64)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)

ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.fit_transform(x_test)

model=linear_model.LogisticRegression()
model.fit(x_train,y_train)
y_predicted=model.predict(x_test)
print("Accuracy:",model.score(x_test,y_test)*100)
y_proba=model.predict_proba(x_test)

sort_order=np.argsort(x_test[:,0])
plt.plot(x_test[:,0][sort_order],y_proba[:,1][sort_order])
plt.show()