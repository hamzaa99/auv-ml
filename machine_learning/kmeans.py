import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

## dossier prenant en compte uniquement les données liées au commerce
villes = pd.read_csv('../data/insee/equip-serv-commerce-com-2020.csv',delimiter=";")



mlcolumns = villes[["NB_B101", "NB_B102","NB_B103","NB_B201","NB_B202","NB_B203","NB_B204","NB_B205","NB_B206","NB_B301","NB_B302","NB_B303","NB_B304","NB_B305","NB_B306","NB_B307","NB_B308","NB_B309","NB_B310","NB_B311","NB_B312","NB_B313","NB_B315","NB_B316"]]

train, test = train_test_split(mlcolumns,test_size=0.2)

kmeans = KMeans(n_clusters=10)
kmeans.fit(train)
labelsKM = kmeans.predict(test)

print(labelsKM)

