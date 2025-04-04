import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('Melbourne_housing_FULL.csv')
df = df.dropna(axis = 0)
y = df.Price
feature = ['Rooms', 'Bathroom','Landsize','BuildingArea','YearBuilt','Lattitude','Longtitude']
X = df[feature]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state= 0)

model = RandomForestRegressor(random_state = 1)
model.fit(train_X,train_y)
pred = model.predict(val_X)
print(mean_absolute_error(val_y,pred))