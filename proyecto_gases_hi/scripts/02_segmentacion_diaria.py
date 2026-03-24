import pandas as pd

df = pd.read_csv("../data/interim/datos_filtrados_ppm.csv")

# Convertir a fecha
df["created_at"] = pd.to_datetime(df["created_at"])

# Crear columna fecha
df["fecha"] = df["created_at"].dt.date

# Guardar base limpia
df.to_csv("../data/processed/datos_limpios.csv", index=False)

# Separar por día
for fecha, grupo in df.groupby("fecha"):
    grupo.to_csv(f"../data/processed/datos_por_dia/{fecha}.csv", index=False)