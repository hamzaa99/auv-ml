import pandas as pd


pop = pd.read_csv("../data/insee/communes.csv",delimiter=";",header=0,index_col=0, dtype={'insee_code': 'str'}, usecols=[0,4])
city = pd.read_csv("../data/insee/cities.csv",delimiter=",",header=0,index_col=2, dtype={'insee_code': 'str'})






print(city.index)
print(pop.index)
global_frame = pd.merge(city,pop,left_index=True, right_index=True)
print(global_frame.head(10))
global_frame = global_frame.sort_values(by=['PTOT'],ascending=False)
print(global_frame.head(10))
global_frame = global_frame.head(20000)
global_frame = global_frame.drop(columns=['PTOT'])
global_frame = global_frame.sort_values(by=['insee_code'],ascending=True)
print(global_frame.index)
global_frame.to_csv('../data/merged/test2.csv')

