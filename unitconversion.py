import pandas as pd
df=pd.read_csv("dwarf_stars.csv")
df=df.dropna()
df["radius"]=0.102763*df["radius"]
df["mass"]=df["mass"].astype("float")
df["mass"]=0.000954588*df["mass"]
df.to_csv("Converted_Dwarf_Stars.csv")
