import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter x values (space seperated): ")
y_input = input("Enter y values (space sperated): ")

x = np.array([float(val) for val in x_input.split()])
y = np.array([float(val) for val in y_input.split()])

mean_x = np.mean(x)
mean_y = np.mean(y)

num = np.sum((x-mean_x)*(y-mean_y))
den = np.sum((x-mean_x)**2)

m = num/den

c = mean_y - (m*mean_x)

y_pred = m*x + c

plt.scatter(x,y,label = "data")
plt.plot(x,y_pred,color = 'red',label = 'reg line')
plt.title("Linear regression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()