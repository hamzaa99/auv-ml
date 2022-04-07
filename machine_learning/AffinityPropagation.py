import pandas as pd
import pickle as pickle
from sklearn.cluster import AffinityPropagation
from sklearn.model_selection import train_test_split

# villes pour à tester
drancy = villes.loc['93029']
laCourneuve = villes.loc['93027']
annecy = villes.loc['74010']
sceaux = villes.loc['92071']
antony = villes.loc['92002']
lyon1 = villes.loc['69381']
lyon2 = villes.loc['69382']
chatillon = villes.loc['92020']

## dossier prenant en compte uniquement les données liées au commerce
villes = pd.read_csv('../data/merged/test.csv',delimiter=",",header=0,index_col='CODGEO', dtype={'CODGEO': 'str'})

affinityModel = AffinityPropagation().fit(villes)


labelsAffinity = affinityModel.predict(villes)

labelDrancy = affinityModel.predict([drancy])
labelLaCourneuve = affinityModel.predict([laCourneuve])
labelAnnecy = affinityModel.predict([annecy])
labelSceaux = affinityModel.predict([sceaux])
labelAntony = affinityModel.predict([antony])
labelChatillon = affinityModel.predict([chatillon])
labelLyon1 = affinityModel.predict([lyon1])
labelLyon2 = affinityModel.predict([lyon2])


print(labelsAffinity)
print(f'le label du cluster de drancy est : {labelDrancy}')
print(f'le label du cluster de laCourneuve est : {labelLaCourneuve}')
print(f'le label du cluster de annecy est : {labelAnnecy}')
print(f'le label du cluster de sceaux est : {labelSceaux}')
print(f'le label du cluster de antony est : {labelAntony}')
print(f'le label du cluster de lyon 1 est : {labelLyon1}')
print(f'le label du cluster de lyon 2 est : {labelLyon2}')
print(f'le label du cluster de chatillon est : {labelChatillon}')


pickle_out = open("../model.pkl", "wb")
pickle.dump(affinityModel, pickle_out)
pickle_out.close()