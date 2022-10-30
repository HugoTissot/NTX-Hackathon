import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import sklearn
import pandas as pd

def PCA(n_components):

    #rows are timesteps
    #columns are bands

    # nbands = 12
    # bands = list(range(nbands))
    bands = ["delta","theta","alpha","beta"]

    calibration_file = "C:/Users/thoma/Documents/GitHub/NTX-Hackathon/src/bands/band_calib.hdf5"

    df = pd.concat([pd.read_hdf(calibration_file,key=key)["A1"] for key in bands],axis=1)
    df.columns = bands

    mat=df.to_numpy()

    pca=sklearn.decomposition.PCA(n_components=n_components,svd_solver='full')

    pca_mat=pca.fit_transform(mat)

    np.save('PCs.npy',pca.components_)
    
    
PCA(3)