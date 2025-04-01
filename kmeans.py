import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')
print(df.head())

x = df.iloc[:, [3,4]].values

scaler = StandardScaler()
scale_x = scaler.fit_transform(x)

inertia = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, init="k-means++",random_state=42)
    kmeans.fit(scale_x)
    inertia.append(kmeans.inertia_)

plt.figure()
plt.plot(range(1,11), inertia, marker = 'o', linestyle='--')
plt.xlabel("no of clusters")
plt.ylabel('inertia')
plt.show()

kmeans = KMeans(n_clusters=5,init='k-means++',random_state=42)
clusters = kmeans.fit_predict(scale_x)

df['clusters'] = clusters

plt.figure()
colors = ['blue','green','purple','orange','brown']

for i in range(5):
    plt.scatter(x[clusters == i,0], x[clusters == i,1], s=100, color = colors[i])

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],s=300,color='red',marker="X")

plt.title("Kmeans clustering")
plt.xlabel("annual")
plt.ylabel('spending')
plt.legend()
plt.show()