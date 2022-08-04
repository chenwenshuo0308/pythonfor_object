from numpy import *

# 从一个文本文件中读入一个数据集,数据集示例如下：
'''
8.805945	10.575145
9.584316	9.614076
11.269714	11.717254
9.120444	9.019774
7.977520	8.313923
'''


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = list(map(float, strline) for strline in stringArr)
    print(type(datArr))
    print(datArr)
    return mat(datArr)


# 基于numpy实现pca算法
def pca(dataMat, topNfeat=9999999):  # 原数据  m*n
    meanVals = mean(dataMat, axis=0)  # 均值：1*n
    meanRemoved = dataMat - meanVals  # 去除均值  m*n
    covMat = cov(meanRemoved, rowvar=0)  # 协方差矩阵 n*n
    eigVals, eigVects = linalg.eig(mat(covMat))  # 特征矩阵  n*n
    eigValInd = argsort(eigVals)  # 将特征值排序
    eigValInd = eigValInd[:-(topNfeat + 1):-1]  # 仅保留p个列（将topNfeat理解为p即可）
    redEigVects = eigVects[:, eigValInd]  # 仅保留p个最大特征值对应的特征向量，按从大到小的顺序重组特征矩阵n*p
    lowDDataMat = meanRemoved * redEigVects  # 将数据转换到低维空间lowDDataMat： m*p
    reconMat = (lowDDataMat * redEigVects.T) + meanVals  # 从压缩空间重构原数据reconMat：  m*n
    return lowDDataMat, reconMat


pca(loadDataSet("dataset.txt"))
