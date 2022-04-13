import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
from sklearn import metrics

## dossier prenant en compte uniquement les données liées au commerce
villes = pd.read_csv('../data/merged/test.csv',delimiter=",",header=0,index_col='CODGEO', dtype={'CODGEO': 'str'})


# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(villes)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)


print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(villes, labels))

drancy = villes.loc['93029']
laCourneuve = villes.loc['93027']
annecy = villes.loc['74010']
sceaux = villes.loc['92071']
antony = villes.loc['92002']
lyon1 = villes.loc['69381']
lyon2 = villes.loc['69382']
chatillon = villes.loc['92020']

print(db.core_sample_indices_)