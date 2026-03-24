import pandas as pd
import matplotlib.pyplot as plt
import os

ruta = "../data/processed/datos_por_dia/"

for archivo in os.listdir(ruta):
    df = pd.read_csv(ruta + archivo)

    fecha = archivo.replace(".csv", "")

    plt.figure()
    plt.plot(df["tiempo_relativo"], df["co2_ppm"])
    plt.title(f"CO2 - {fecha}")
    plt.savefig(f"../figures/diarios/{fecha}_co2.png")
    plt.close()

    plt.figure()
    plt.plot(df["tiempo_relativo"], df["ch4_ppm"])
    plt.title(f"CH4 - {fecha}")
    plt.savefig(f"../figures/diarios/{fecha}_ch4.png")
    plt.close()