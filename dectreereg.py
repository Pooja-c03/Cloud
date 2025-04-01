import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('Melbourne_housing_FULL.csv')
df = df.dropna(subset = ['Price','Rooms','Distance','Propertycount'])
feature = ['Rooms','Distance','Propertycount']
X = df[feature]
y = df['Price']

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(train_X,train_y)
pred = model.predict(test_X)
print(mean_absolute_error(test_y,pred))