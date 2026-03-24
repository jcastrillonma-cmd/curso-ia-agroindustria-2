import pandas as pd
import os

ruta = "../data/processed/datos_por_dia/"

for archivo in os.listdir(ruta):
    if archivo.endswith(".csv"):
        df = pd.read_csv(ruta + archivo)

        # Asegurar formato datetime
        df["created_at"] = pd.to_datetime(df["created_at"])

        # Calcular tiempo relativo
        df["tiempo_relativo"] = (
            df["created_at"] - df["created_at"].min()
        ).dt.total_seconds()

        # Guardar archivo actualizado
        df.to_csv(ruta + archivo, index=False)

print("Alineación temporal lista")