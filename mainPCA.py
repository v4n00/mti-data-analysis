import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

with open('util/datasetPCA.py', 'r') as f:
    exec(f.read())

class PCA:
    def __init__(self, X):
        self.X = X
        self.Cov = np.cov(self.X, rowvar=False)
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(self.Cov)
        k_desc = [k for k in reversed(np.argsort(self.eigenvalues))]
        self.alpha = self.eigenvalues[k_desc]
        self.a = self.eigenvectors[:, k_desc]
        self.C = self.X @ self.a
        self.Rxc = self.a * np.sqrt(self.alpha)
        self.scores = self.C / np.sqrt(self.alpha)
        self.C2 = self.C * self.C
        C2SL = np.sum(self.C2, axis=1)
        self.quality = np.transpose(self.C2.T / C2SL)

    def getAlpha(self):
        return self.alpha
    def getA(self):
        return self.a
    def getPrinComp(self):
        return self.C
    def getFactorLoadings(self):
        return self.Rxc
    def getScores(self):
        return self.scores
    def getQualityOfPoints(self):
        return self.quality
    def getContributions(self):
        return self.C2 / (self.X.shape[0] * self.alpha)
    def getCommonalities(self):
        Rxc2 = np.square(self.Rxc)
        return np.cumsum(a=Rxc2, axis=1)
    def getCumulativeVariance(self):
        return np.cumsum(self.alpha) / np.sum(self.alpha)


def correlogram(matrix=None, dec=2, title='Correlogram', valmin=-1, valmax=1):
    plt.figure(title, figsize=(16, 11))
    plt.title(title, fontsize=16, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrix, dec), vmin=valmin, vmax=valmax, cmap='bwr', annot=True)

def principalComponents(eigenvalues=None, XLabel='Principal components', YLabel='Eigenvalues (variance)', title='Explained variance by the principal components'):
    plt.figure(title, figsize=(13, 8))
    plt.title(title, fontsize=14, color='k', verticalalignment='bottom')
    plt.xlabel(XLabel, fontsize=14, color='k', verticalalignment='top')
    plt.ylabel(YLabel, fontsize=14, color='k', verticalalignment='bottom')
    components = ['C'+str(j+1) for j in range(eigenvalues.shape[0])]
    plt.plot(components, eigenvalues, 'bo-')
    plt.axhline(y=1, color='r')

table = pd.read_csv('./dataIN/thyroid_dataset_pca.csv', index_col=0)
table.reset_index(inplace=True)

obs = table.index.values
vars = table.columns.values[0:14]
X = table[vars].values
X_df = pd.DataFrame(data=X, index=obs, columns=vars)

# PCA model
pcaModel = PCA(X)
alpha = pcaModel.getAlpha()

# creating the graphic of eigenvalues
principalComponents(eigenvalues=alpha)

# save the principal components
C = pcaModel.getPrinComp()
nameC = ['C'+str(j+1) for j in range(C.shape[1])]
C_df = pd.DataFrame(data=C, index=obs, columns=nameC)
C_df.to_csv('./dataOUT/PCA/princComp.csv')
plt.savefig('./dataOUT/PCA/principal_components.png')

# fetch the factor loadings
factorLoadings = pcaModel.getFactorLoadings()
factorLoadings_df = pd.DataFrame(data=factorLoadings, index=vars, columns=nameC)
factorLoadings_df.to_csv('./dataOUT/PCA/factorLoadings.csv')

# create the correlogram for correlation between the initial variables and principal components
correlogram(matrix=factorLoadings_df, title='The correlation between the initial variables and principal components')
plt.savefig('./dataOUT/PCA/factor_loadings.png')

# rest of the PCA data
scores = pcaModel.getScores()
scores_df = pd.DataFrame(data=scores, index=obs, columns=nameC)
scores_df.to_csv('./dataOUT/PCA/scores.csv')

qualityOfPoints = pcaModel.getQualityOfPoints()
qualityOfPoints_df = pd.DataFrame(data=qualityOfPoints, index=obs, columns=nameC)
qualityOfPoints_df.to_csv('./dataOUT/PCA/quality.csv')

common = pcaModel.getCommonalities()
common_df = pd.DataFrame(data=common, index=vars, columns=nameC)
common_df.to_csv('./dataOUT/PCA/commonalities.csv')

plt.show()