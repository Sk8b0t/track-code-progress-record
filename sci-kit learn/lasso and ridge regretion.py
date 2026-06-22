from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris=datasets.load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['target']=iris.target
df.rename(columns={'sepal length (cm)':'sepal_length',
                          'sepal width (cm)':'sepal_width',
                          'petal length (cm)':'petal_length',
                          'petal width (cm)':'petal_width'},inplace=True)
df['species']= df['target'].replace({
    0:'sesota',
    1:'versicolor',
    2:'virginica'
})

data=df.loc[df['target']==1]
x=data['petal_length'].values.reshape(-1,1)
y=data['petal_width'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=1)

model=linear_model.Lasso(alpha=0.01)
model.fit(x_train,y_train)
y_predicted=model.predict(x_test)
print("slope as per lasso regretion=",model.coef_)

model1=linear_model.LinearRegression()
model1.fit(x_train,y_train)
y_predicted1=model1.predict(x_test)
print("slope as per linear regession:",model1.coef_)

model2=linear_model.Ridge(alpha=1.5)
model2.fit(x_train,y_train)
y_predicted2=model2.predict(x_test)
print("slope as per ridge regession:",model2.coef_)

plt.scatter(x_test,y_test)
plt.plot(x_test,y_predicted2)
plt.show()



# plt.scatter(x_test,y_test)
# plt.plot(x_test,y_predicted)
# plt.plot(x_test,y_predicted1)
plt.show()

