from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# =========================
# Rutas base
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

input_dir = BASE_DIR / "data/processed/datos_por_dia"
output_diarios = BASE_DIR / "figures/diarios"
output_comparativos = BASE_DIR / "figures/comparativos"
bitacora_path = BASE_DIR / "reports/bitacora_limpieza.md"

# Crear carpetas
output_diarios.mkdir(parents=True, exist_ok=True)
output_comparativos.mkdir(parents=True, exist_ok=True)

# =========================
# Archivos diarios
# =========================
archivos = sorted(input_dir.glob("*.csv"))

archivos_generados = []
comparativos_generados = []

# =========================
# 1. GRÁFICOS DIARIOS
# =========================
for archivo in archivos:
    df = pd.read_csv(archivo)
    fecha = archivo.stem

    # ---- CO2 ----
    plt.figure()
    plt.plot(df["tiempo_relativo_min"], df["co2_ppm"])
    plt.xlabel("Tiempo (min)")
    plt.ylabel("CO2 (ppm)")
    plt.title(f"CO2 - {fecha}")

    ruta_co2 = output_diarios / f"{fecha}_co2.png"
    plt.savefig(ruta_co2)
    plt.close()
    archivos_generados.append(ruta_co2.name)

    # ---- CH4 ----
    plt.figure()
    plt.plot(df["tiempo_relativo_min"], df["ch4_ppm"])
    plt.xlabel("Tiempo (min)")
    plt.ylabel("CH4 (ppm)")
    plt.title(f"CH4 - {fecha}")

    ruta_ch4 = output_diarios / f"{fecha}_ch4.png"
    plt.savefig(ruta_ch4)
    plt.close()
    archivos_generados.append(ruta_ch4.name)

    # ---- CONJUNTO ----
    plt.figure()
    plt.plot(df["tiempo_relativo_min"], df["co2_ppm"], label="CO2")
    plt.plot(df["tiempo_relativo_min"], df["ch4_ppm"], label="CH4")
    plt.xlabel("Tiempo (min)")
    plt.ylabel("Concentración (ppm)")
    plt.title(f"CO2 vs CH4 - {fecha}")
    plt.legend()

    ruta_conjunto = output_diarios / f"{fecha}_conjunto.png"
    plt.savefig(ruta_conjunto)
    plt.close()
    archivos_generados.append(ruta_conjunto.name)

# =========================
# 2. GRÁFICOS COMPARATIVOS
# =========================

# ---- CO2 comparativo ----
plt.figure()
for archivo in archivos:
    df = pd.read_csv(archivo)
    fecha = archivo.stem
    plt.plot(df["tiempo_relativo_min"], df["co2_ppm"], label=fecha)

plt.xlabel("Tiempo (min)")
plt.ylabel("CO2 (ppm)")
plt.title("CO2 - Comparación entre días")
plt.legend()

ruta_co2_comp = output_comparativos / "co2_todos_los_dias.png"
plt.savefig(ruta_co2_comp)
plt.close()
comparativos_generados.append(ruta_co2_comp.name)

# ---- CH4 comparativo ----
plt.figure()
for archivo in archivos:
    df = pd.read_csv(archivo)
    fecha = archivo.stem
    plt.plot(df["tiempo_relativo_min"], df["ch4_ppm"], label=fecha)

plt.xlabel("Tiempo (min)")
plt.ylabel("CH4 (ppm)")
plt.title("CH4 - Comparación entre días")
plt.legend()

ruta_ch4_comp = output_comparativos / "ch4_todos_los_dias.png"
plt.savefig(ruta_ch4_comp)
plt.close()
comparativos_generados.append(ruta_ch4_comp.name)

# =========================
# 3. BITÁCORA (TODO DENTRO)
# =========================
with open(bitacora_path, "a", encoding="utf-8") as f:
    f.write("\n\n## 03 - Generación de gráficos\n")
    f.write(f"- Fecha de ejecución: {datetime.now()}\n")
    f.write(f"- Carpeta de entrada: {input_dir}\n")
    f.write(f"- Carpeta de salida (diarios): {output_diarios}\n")
    f.write(f"- Carpeta de salida (comparativos): {output_comparativos}\n")

    f.write("- Transformaciones aplicadas:\n")
    f.write("  - Gráficos diarios de CO2\n")
    f.write("  - Gráficos diarios de CH4\n")
    f.write("  - Gráficos conjuntos CO2 vs CH4\n")
    f.write("  - Gráficos comparativos entre días\n")
    f.write("  - Uso de tiempo relativo como eje temporal\n")

    f.write(f"- Número de días procesados: {len(archivos)}\n")

    f.write("- Archivos generados (diarios):\n")
    for archivo in archivos_generados:
        f.write(f"  - {archivo}\n")

    f.write("- Archivos generados (comparativos):\n")
    for archivo in comparativos_generados:
        f.write(f"  - {archivo}\n")

    f.write("- Justificación técnica:\n")
    f.write("  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.\n")