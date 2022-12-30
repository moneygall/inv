import pandas as pd

d= pd.read_excel("tgt.xlsx", header=None, names=["id",])
print(d["id"].values.tolist())