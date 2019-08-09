#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Pull in code that will make all this happen

# packages for kmeans
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import datasets

# Familiar packages for plotting, data manipulation, and numeric functions
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Have plots appear in notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Default plot params
plt.style.use('seaborn')
cmap = 'tab10'


"""
The purpose of this small suite of functions is to clean up my image creation code in the notebook.
Also I need to practice what I preach to my students about using scripts to house my complex messy code.


These functions create sample datasets and images to demonstrate how kmeans will work in ideal and non-ideal scenarios.
"""

def ideal():
    """Example of a nice and tidy dataset that kmeans will LIKE"""
    #make data
    centers_neat = [(-10, 10), (0, -5), (10, 5)]
    x_neat, _ = datasets.make_blobs(n_samples=5000,
                                centers=centers_neat,
                                cluster_std=2,
                                random_state=2)
    #fit k-means
    km_neat = KMeans(n_clusters=3, random_state=2).fit_predict(x_neat)
    
    # plot
    plt.figure(figsize=(15,8))
    plt.subplot(121, title='Ideal K-Means')
    plt.scatter(x_neat[:,0], x_neat[:,1])
    plt.show()
    
    

def messyOne():
    """Creates a scenario that does not play well with kmeans"""
    x_messy, labs3 = datasets.make_classification(n_samples=5000,
                                         n_features=10,
                                          n_classes=3,
                                          n_clusters_per_class=1,
                                          class_sep=1.5,
                                          shuffle=False,
                                          random_state=301)
    km_messy = KMeans(n_clusters=3, random_state=2).fit_predict(x_messy)
    km_messy2 = KMeans(n_clusters=3, random_state=2).fit(x_messy)
    
    plt.figure(figsize=(15,8))
    plt.subplot(121, title='Problem Cluster Example 1')
    plt.scatter(x_messy[:,0], x_messy[:,1], c=labs3,  cmap=cmap)
    plt.subplot(122, title='Problem Cluster Example 1 K-means labels')
    plt.scatter(x_messy[:,0], x_messy[:,1], c=km_messy, cmap=cmap)
    plt.scatter(km_messy2.cluster_centers_[:,0], km_messy2.cluster_centers_[:,1], marker='X', s=150, c='black')
    
    plt.show()
    
def messyTwo():
    """Creates another messy dataset that doesn't play well with kmeans"""
    # Second toy data set
    blob1, y1 = datasets.make_blobs(n_samples=25,
                               centers=[(10,5)],
                               cluster_std=1.5,
                               random_state=2)

    blob2, y2 = datasets.make_blobs(n_samples=500,
                               centers=[(6,2)],
                               cluster_std=1.3,
                               random_state=2)

    blob3, y3 = datasets.make_blobs(n_samples=500,
                               centers=[(2,5)],
                               cluster_std=1,
                               random_state=2)

    unbal = np.vstack([blob1, blob2, blob3])
    y1[y1 == 0] = 0
    y2[y2 == 0] = 1
    y3[y3 == 0] = 2
    labs = np.concatenate([y1, y2, y3])

    #Predict K-Means cluster membership
    km_unbal = KMeans(n_clusters=3, random_state=2).fit(unbal)
    km_unbal_preds = KMeans(n_clusters=3, random_state=2).fit_predict(unbal)

    plt.figure(figsize=(15,8))
    plt.subplot(121, title= 'Problem Clusters Example 2')
    plt.scatter(unbal[:,0], unbal[:,1], c=labs, cmap=cmap)
    plt.subplot(122, title='Problem Clusters Example 2 K-means labels')
    plt.scatter(unbal[:,0], unbal[:,1], c=km_unbal_preds, cmap=cmap)
    plt.scatter(km_unbal.cluster_centers_[:,0], km_unbal.cluster_centers_[:,1], marker='X', s=150, c='black')
    
    plt.show()


def messyThree():
    # Problem Scenario 3

    # Third toy data set
    blob1, y1 = datasets.make_blobs(n_samples=100,
                                   centers=[(10,8)],
                                   cluster_std=0.5,
                                   random_state=2)

    blob2, y2 = datasets.make_blobs(n_samples=600,
                                   centers=[(2,2)],
                                   cluster_std=2.5,
                                   random_state=2)


    unbal = np.vstack([blob1, blob2])
    y1[y1 == 0] = 0
    y2[y2 == 0] = 1
    labs = np.concatenate([y1, y2])

    #Predict K-Means cluster membership
    km_unbal = KMeans(n_clusters=2, random_state=2).fit(unbal)
    km_unbal_preds = KMeans(n_clusters=2, random_state=2).fit_predict(unbal)

    plt.figure(figsize=(15,8))
    plt.subplot(121, title='Problem Clusters Example 3')
    plt.scatter(unbal[:,0], unbal[:,1])
    plt.subplot(122, title='Problem Clusters Example 3 K-means labels')
    plt.scatter(unbal[:,0], unbal[:,1], c=km_unbal_preds, cmap=cmap)
    plt.scatter(km_unbal.cluster_centers_[:,0], km_unbal.cluster_centers_[:,1], marker='X', s=150, c='black')
    plt.show()

