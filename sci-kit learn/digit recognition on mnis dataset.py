from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
# from cuml.linear_model import LogisticRegression
import matplotlib
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

mnist=fetch_openml('mnist_784')
x=mnist['data'].loc[:1000,:]
y=mnist['target'].loc[:1000].astype(int)

# plt.imshow(x.loc[322].to_numpy().reshape(28,28),cmap=matplotlib.cm.binary,interpolation="nearest")
# print(y.loc[322])
# plt.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
y_train_2=(y_train==2)
y_test_2=(y_test==2)

clf=LogisticRegression(tol=0.1)
clf.fit(x_train,y_train_2)
y_pred_2=clf.predict(x_test)
print(f"Accuracy: {clf.score(x_test,y_test_2)*100:.2f}%")

accur=cross_val_score(clf,x,y,cv=3,scoring='accuracy')
print(accur.mean())

conmat=confusion_matrix(y_test_2,y_pred_2)
print(conmat)

print("precision=",precision_score(y_test_2,y_pred_2))
print("recall",recall_score(y_test_2,y_pred_2))
print("f-1 score=",f1_score(y_test_2,y_pred_2))

