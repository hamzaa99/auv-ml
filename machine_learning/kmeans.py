import pandas as pd
import pickle as pickle
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

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



kmeans = KMeans(10)

kmeans.fit(villes)

labelsKM = kmeans.predict(villes)

labelDrancy = kmeans.predict([drancy])
labelLaCourneuve = kmeans.predict([laCourneuve])
labelAnnecy = kmeans.predict([annecy])
labelSceaux = kmeans.predict([sceaux])
labelAntony = kmeans.predict([antony])
labelChatillon = kmeans.predict([chatillon])
labelLyon1 = kmeans.predict([lyon1])
labelLyon2 = kmeans.predict([lyon2])


print(labelsKM)
print(f'le label du cluster de drancy est : {labelDrancy}')
print(f'le label du cluster de laCourneuve est : {labelLaCourneuve}')
print(f'le label du cluster de annecy est : {labelAnnecy}')
print(f'le label du cluster de sceaux est : {labelSceaux}')
print(f'le label du cluster de antony est : {labelAntony}')
print(f'le label du cluster de lyon 1 est : {labelLyon1}')
print(f'le label du cluster de lyon 2 est : {labelLyon2}')
print(f'le label du cluster de chatillon est : {labelChatillon}')


pickle_out = open("../api/model.pkl", "wb")
pickle.dump(kmeans, pickle_out)
pickle_out.close()