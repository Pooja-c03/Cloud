import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

iris = datasets.load_iris()
X = iris.data
y = iris.target

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
train_X = scaler.fit_transform(train_X)
test_X = scaler.transform(test_X)

model = LogisticRegression(multi_class='ovr', solver='lbfgs', max_iter=200)
model.fit(train_X,train_y)

pred = model.predict(test_X)

print(accuracy_score(test_y, pred))
print(classification_report(test_y,pred,target_names=iris.target_names))