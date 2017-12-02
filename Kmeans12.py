#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:52:30 2017

@author: sabarnikundu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

dataset=pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,[3,4]].values

#using elbow method to find the clusters
from sklearn.cluster import KMeans
wcss= []
for i in range(1,11):
    kmeans= KMeans(n_clusters= i, init= 'k-means++', n_init=10, max_iter=300, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('no. of clusters')
plt.ylabel('wcss')
plt.show()

kmeans= KMeans(n_clusters= 5, init= 'k-means++' , n_init= 10, max_iter= 300 , random_state=0)
y_means= kmeans.fit_predict(X)

#visualising the plot
plt.scatter(X[y_means== 0, 0 ], X[y_means== 0, 1], s=100, c='red', label= 'cluster1')
plt.scatter(X[y_means== 1, 0 ], X[y_means== 1, 1], s=100, c='blue', label= 'cluster2')
plt.scatter(X[y_means== 2, 0 ], X[y_means== 2, 1], s=100, c='yellow', label= 'cluster3')
plt.scatter(X[y_means== 3, 0 ], X[y_means== 3, 1], s=100, c='magenta', label= 'cluster4')
plt.scatter(X[y_means== 4, 0 ], X[y_means== 4, 1], s=100, c='purple', label= 'cluster5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300, c='cyan', label='centroid')
plt.title('clusters')
plt.ylabel('spending score')
plt.xlabel('annual income')
plt.legend()
plt.show()
