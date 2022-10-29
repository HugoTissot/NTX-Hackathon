import pandas as pd

path12 = '../NTX-Hackathon/src/bands/bands12_calib.hdf5'
path4 = '../NTX-Hackathon/src/bands/bands4_calib.hdf5'

bands12 = [f'P{i}' for i in range(12)]
bands4 = ['delta','theta','alpha','beta']


df = pd.concat([pd.read_hdf(bands4,key=key)["A1"] for key in bands4],axis=1)
df.columns = bands4
# df = pd.concat([pd.read_hdf(bands12,key=key)["A1"] for key in bands12],axis=1)
# df.columns = bands12