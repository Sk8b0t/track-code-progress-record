from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

dia=datasets.load_diabetes()
#['data','target','frame','DESCR','feature_names','data_filename','target_filename', 'data_module']
print(dia.keys())
# print(dia.DESCR)

dia_bmi_x=dia.data[:,np.newaxis,2]
dia_bmi_x_train=dia_bmi_x[:-30]
dia_bmi_x_test=dia_bmi_x[-20:]

dia_bmi_y_train=dia.target[:-30]
dia_bmi_y_test=dia.target[-20:]

mod=linear_model.LinearRegression()
mod.fit(dia_bmi_x_train,dia_bmi_y_train)

dia_y_predicted=mod.predict(dia_bmi_x_test)
print("Mean squared error:",mean_squared_error(dia_y_predicted,dia_bmi_y_test))
print("Weights:",mod.coef_)
print("Intercept:",mod.intercept_)

plt.scatter(dia_bmi_x_test,dia_bmi_y_test)
plt.plot(dia_bmi_x_test,dia_y_predicted)
plt.show()

