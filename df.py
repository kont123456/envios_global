import pandas as pd

df=pd.read_excel("C:\\Users\\luis\\Desktop\\PYTHOM PROGRAMAS\\Avanzado\\Plantilla.xlsx")
df["Año"]=df["Fecha_envio"].dt.year.astype(str)
df["Mes"]=df["Fecha_envio"].dt.month




