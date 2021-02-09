from numpy import *
datMat = mat([[1,2,3],[4,NAN,6]])
numFeat = shape(datMat)[1]
for i in range(numFeat):

    meanVal = mean(datMat[nonzero(~isnan(datMat[:,i]))[0],i])
    #values that are not NaN (a number)
    datMat[nonzero(isnan(datMat[:,i]))[0],i] = meanVal
  #set NaN values to mean
print(datMat)