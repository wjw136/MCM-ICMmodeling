evalue=[[-123.943134 ,    63.82378203 ,  44.13805117],
 [-122.581335  ,  138.38446567  ,109.75395567],
 [-122.418612  ,  144.39688619 , 120.20634567],
 [-122.745016 ,   117.31779441 , 124.15313847],
 [-122.641648 ,   132.49061196 , 124.34322941],
 [-122.700941  ,  157.60111866 , 139.99316194],
 [-122.582465  ,  154.94646534 , 146.31122309],
 [-122.661037 ,   143.86489732  ,146.82921424],
 [-122.702242 ,   180.11293896 , 188.44429822],
 [-122.688503  ,  113.4677369  ,  88.62933482]];
from sklearn.cluster import KMeans
import multiprocessing
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import scipy
import numpy as np
fscore=[]
import  math
cl_centers=[[-122.629162  ,  146.13939731 , 137.50432084],
 [-123.3158185  ,  88.64575946  , 66.38369299]]
def getd(p1,p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    # 用math.sqrt（）求平方根
    return  math.sqrt((x ** 2) + (y ** 2)+ (z ** 2))
for i in range(10):
    print(max(getd(evalue[i],cl_centers[0]),getd(evalue[i],cl_centers[1])))