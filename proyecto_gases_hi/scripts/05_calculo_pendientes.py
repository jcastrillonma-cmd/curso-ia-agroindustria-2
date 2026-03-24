import pandas as pd
import numpy as np
import os

resultados = []

ruta = "../data/processed/datos_por_dia/"

for archivo in os.listdir(ruta):
    df = pd.read_csv(ruta + archivo)

    x = df["tiempo_relativo"]

    pendiente_co2 = np.polyfit(x, df["co2_ppm"], 1)[0]
    pendiente_ch4 = np.polyfit(x, df["ch4_ppm"], 1)[0]

    resultados.append([archivo, pendiente_co2, pendiente_ch4])

df_res = pd.DataFrame(resultados, columns=["fecha", "pendiente_co2", "pendiente_ch4"])
df_res.to_csv("../data/processed/resumen_pendientes.csv", index=False)