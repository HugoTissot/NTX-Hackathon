import pandas as pd

# nbands = 12
# bands = list(range(nbands))
bands = ["delta","theta","alpha","beta"]

calibration_file = "./bands/band_calib.hdf5"

df = pd.concat([pd.read_hdf(calibration_file,key=key)["A1"] for key in bands],axis=1)
df.columns = bands