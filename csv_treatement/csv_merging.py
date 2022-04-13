import pandas as pd

commerce = pd.read_csv("../data/insee/equip-serv-commerce-com-2020.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'})
ens = pd.read_csv("../data/insee/equip-serv-ens-1er-degre-com-2020.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'})
ens_sup = pd.read_csv("../data/insee/equip-serv-ens-sup-form-serv-com-2020.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'})
sport_loisir = pd.read_csv("../data/insee/equip-sport-loisir-socio-com-2020.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'})
tourisme = pd.read_csv("../data/insee/equip-tour-transp-com-2020.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'})
pop = pd.read_csv("../data/insee/communes.csv",delimiter=";",header=0,index_col=0, dtype={'CODGEO': 'str'}, usecols=[0,4])

frames = [commerce, ens, ens_sup, sport_loisir, tourisme,pop]



global_frame = pd.merge(commerce,ens,left_index=True, right_index=True)
global_frame = pd.merge(commerce,ens_sup,left_index=True, right_index=True)

# global_frame = pd.merge(global_frame,ens_sup,left_index=True, right_index=True)
global_frame = pd.merge(global_frame,sport_loisir,left_index=True, right_index=True)
#
global_frame = pd.merge(global_frame,tourisme,left_index=True, right_index=True)
global_frame = pd.merge(global_frame,pop,left_index=True, right_index=True)


global_frame = global_frame.sort_values(by=['PTOT'],ascending=False)
print(global_frame.head(10))
global_frame = global_frame.head(20000)
global_frame = global_frame.sort_values(by=['CODGEO'])
print(global_frame.index)
global_frame.to_csv('../data/merged/test.csv')

