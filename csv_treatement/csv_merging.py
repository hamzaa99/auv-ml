import pandas as pd

commerce = pd.read_csv("../data/insee/equip-serv-commerce-com-2020.csv")
ens = pd.read_csv("../data/insee/equip-serv-ens-1er-degre-com-2020.csv")
ens_sup = pd.read_csv("../data/insee/equip-serv-ens-sup-form-serv-com-2020.csv")
sport_loisir = pd.read_csv("../data/insee/equip-sport-loisir-socio-com-2020.csv")
tourisme = pd.read_csv("../data/insee/equip-tour-transp-com-2020.csv")


frames = [commerce, ens, ens_sup, sport_loisir, tourisme]

global_frame = pd.concat(frames,axis=1)

global_frame.to_csv('../data/merged/test.csv')


print(global_frame.head)