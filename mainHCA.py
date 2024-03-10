import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hic
import scipy.spatial.distance as dis

with open('util/datasetHCA.py', 'r') as f:
  exec(f.read())

def dendrogram(h, labels, title='Hierarchical Classification', threshold=None):
    plt.figure(figsize=(15, 8))
    plt.title(title, fontsize=16, color='k')
    hic.dendrogram(h, labels=labels, leaf_rotation=30)
    if threshold:
        plt.axhline(threshold, c='r')

def threshold(h):
    m = np.shape(h)[0]
    dist_1 = h[1:m, 2]
    dist_2 = h[0:m - 1, 2]
    diff = dist_1 - dist_2
    j = np.argmax(diff)
    threshold = (h[j, 2] + h[j + 1, 2]) / 2
    return threshold, j, m


# determine the clusters of the maximum stability partition
def clusters(h, k):
    n = np.shape(h)[0] + 1
    g = np.arange(0, n)
    for i in range(n - k):
        k1 = h[i, 0]
        k2 = h[i, 1]
        g[g == k1] = n + i
        g[g == k2] = n + i
    cat = pd.Categorical(g)
    return ['C'+str(i) for i in cat.codes], cat.codes

startIdx = 10
endIdx = 64

table = pd.read_csv('dataIN/thyroid_dataset_hca.csv', index_col=0, na_values='')
obsName = table.index[startIdx:endIdx]
X = table.iloc[startIdx:endIdx, :].values

methods = list(hic._LINKAGE_METHODS)
distances = dis._METRICS_NAMES

method = 5
distance = 7
HC = hic.linkage(X, method=methods[method], metric=distances[distance])
t, j, m = threshold(HC)
with open('./dataOUT/HCA/result.txt', 'w') as file:
    file.write('threshold = ' + str(t) + '\njunction with max. diff = ' + str(j) + '\nno. of junctions = ' + str(m))

k = m - j
dendrogram(HC, labels=obsName, title='Hierarchical Classification ' + methods[method] + ' - ' + distances[distance], threshold=t)
plt.savefig('./dataOUT/HCA/hierarchical_classification.png')

# determine the clusters belonging to the maximum stability partition
labels, codes = clusters(HC, k)
ClusterTab = pd.DataFrame(data=labels, index=obsName, columns=['Cluster'])
ClusterTab.to_csv('dataOUT/HCA/indClusters.csv')

plt.show()