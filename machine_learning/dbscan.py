import pandas as pd
import pickle as pickle
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN
from matplotlib import pyplot

## dossier prenant en compte uniquement les données liées au commerce
villes = pd.read_csv('../data/merged/test.csv',delimiter=",",header=0,index_col='CODGEO', dtype={'CODGEO': 'str'})


# print(villes.head())
# print(villes.dtypes)
drancy = villes.loc['93029']
laCourneuve = villes.loc['93027']
annecy = villes.loc['74010']
sceaux = villes.loc['92071']
antony = villes.loc['92002']
lyon1 = villes.loc['69381']
lyon2 = villes.loc['69382']
chatillon = villes.loc['92020']


model = DBSCAN(eps=0.30, min_samples=9)
yhat = model.fit_predict(villes)
clusters = unique(yhat)
for cluster in clusters:
	row_ix = where(yhat == cluster)
	pyplot.scatter(villes[row_ix, 0], villes[row_ix, 1])
pyplot.show()
