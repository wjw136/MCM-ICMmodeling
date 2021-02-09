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
#Silhouette Coefficient max best
def train_cluster(train_vecs, model_name=None, start_k=2, end_k=10):
    print('training cluster')
    scores = []
    models = []
    for i in range(start_k, end_k):
        kmeans_model = KMeans(n_clusters=i, n_jobs=multiprocessing.cpu_count(), )
        kmeans_model.fit(train_vecs)
        score = silhouette_score(train_vecs,kmeans_model.labels_,metric='euclidean')
        scores.append(score)  # 保存每一个k值的score值, 在这里用欧式距离
        print('{} Means score loss = {}'.format(i, score))
        models.append(kmeans_model)
    plt.plot(range(2,10),scores,'b*-')
    # 设置横纵坐标的名称以及对应字体格式
    font2 = {'family': 'SimHei',
             'weight': 'normal',
             'size': 30,
             }
    plt.xlabel('n_clusters', font2)
    plt.ylabel('score', font2)
    plt.title('for best n_clusters',font2)
    plt.xticks(rotation=-15)  # 设置x轴标签旋转角度
    plt.savefig('for best n.jpg')
    plt.show()
    best_model = models[scores.index(max(scores))]
    return best_model
kmeans_results=train_cluster(evalue)
cl_centers = kmeans_results.cluster_centers_
print(cl_centers)
fscore=[]
import  math
def getd(p1,p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    # 用math.sqrt（）求平方根
    return  math.sqrt((x ** 2) + (y ** 2)+ (z ** 2))
for i in evalue:
    print(max(getd(evalue[i],cl_centers[0]),getd(evalue[i],cl_centers[1])))