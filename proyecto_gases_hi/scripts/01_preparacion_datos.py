import pandas as pd

# Leer datos
df = pd.read_csv("../data/raw/datosbase.csv")

# Seleccionar columnas
df = df[["created_at", "entry_id", "field2", "field4"]]

# Renombrar
df = df.rename(columns={
    "field2": "co2_ppm",
    "field4": "ch4_ppm"
})

# Guardar
df.to_csv("../data/interim/datos_filtrados_ppm.csv", index=False)
