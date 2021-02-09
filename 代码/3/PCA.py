import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
def standardization(dataX):
###pca程序1 ，准备程序
    meanVal=dataX.mean(axis=0)        ###我们的数据变量按列进行排列(即一行为一个样本),按列求均值，即求各个特征的均值
    #meanVal = np.mean(dataX, axis=0) ###此同为np的方法,得到Series
    stdVal=dataX.std(axis=0)
    datasTad =(dataX-meanVal)/stdVal
    return datasTad
## Given cumulative interpretation rate, principal component selection is determined
def pcaPercentage(dataX,datasTad,percentage= 0.85):
#pca 程序2，主程序
    dataCov = datasTad.cov()
    newData1 = np.array(dataCov)
    eigenValue, eigenVector = np.linalg.eig(newData1)#求得特征值，特征向量
    sortEigenValue = np.argsort(eigenValue)         #特征值下标从小到大的排列顺序
    sorceEigenValue=np.sort(eigenValue)             #升序
    cumEigenValue = np.cumsum(sorceEigenValue)      #特征值累加
    sumEigenValue= sum(sorceEigenValue)             #特征值求和
    k =0                                            #计数，k最终结果为对应要提取的主成份个数
    for i in cumEigenValue:
        k = k+1
        if i >=sumEigenValue*percentage:
            break
    nPcaEigenVector = sorceEigenValue[-k:]
    pcaEigenVector = eigenVector[nPcaEigenVector]    #选取特征值对应的特征向量
    PCAX = np.dot(dataX , pcaEigenVector.T)          #得到降维后的数据
    return PCAX ,pcaEigenVector,k
from numpy import *
def pcan(dataX,datasTad,n):
#pca 程序2，主程序
    dataCov = datasTad.cov()
    newData1 = np.array(dataCov)
# means filling
    mean=np.mean(newData1)
    if(np.isnan(mean)):
        numFeat = shape(newData1)[1]
        for i in range(numFeat):
            newData1[i]=0
    else:
        numFeat = shape(newData1)[1]
        for i in range(numFeat):
            if np.isnan(newData1[i]):
                newData1[i]=mean

    eigenValue, eigenVector = np.linalg.eig(newData1)
    sorceEigenValue = np.argsort(eigenValue)
    nPcaEigenVector = sorceEigenValue[-n:]
    pcaEigenVector = eigenVector[nPcaEigenVector]
    PCAX = np.dot(dataX , pcaEigenVector.T)
    return PCAX ,pcaEigenVector



#     导入数据，切记不含因变量。我们在此构造df1数据，此数据变量间没有一定的相关性，只做计算演示。
df1 = pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\代码\3\dataforPCA.xlsx')
datasTad = standardization(df1)
PCAX, pcaEigenVector = pcan(df1, datasTad, 3)  # 指定k,选取主成份
#PCAX,pcaEigenVector ,k =pcaPercentage(df1,datasTad,percentage= 0.85)#根据累计解释率来确定主成分
print (pcaEigenVector)
print (PCAX)
px=PCAX[:,0]
py=PCAX[:,1]
pz=PCAX[:,2]
print(px)
print(py)
print(pz)



