import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x_input = input("Enter x values (space seperated): ")
y_input = input("Enter y values (space seperated): ")

x = np.array([float(val) for val in x_input.split(",")]).reshape(-1,1)
y = np.array([float(val) for val in y_input.split(",")])

if len(x) != len(y):
    print("ERROR! No. of values should match.")
else:
    model = LinearRegression()
    model.fit(x,y)
    m = model.coef_[0]
    c = model.intercept_
    y_pred = model.predict(x)

    plt.scatter(x,y,label = 'data points')
    plt.plot(x,y_pred,color = 'red', label = 'reg line')
    plt.title("Linear Regression")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()
