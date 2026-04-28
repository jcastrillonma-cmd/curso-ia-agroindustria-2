from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

# =========================
# Rutas
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

input_dir = BASE_DIR / "data/processed/datos_por_dia"
output_path = BASE_DIR / "data/processed/resumen_pendientes.csv"
bitacora_path = BASE_DIR / "reports/bitacora_limpieza.md"

# =========================
# Archivos diarios
# =========================
archivos = sorted(input_dir.glob("*.csv"))

resultados = []

# =========================
# Función de pendiente
# =========================
def calcular_pendiente(x, y):
    if len(x) < 2:
        return np.nan
    return np.polyfit(x, y, 1)[0]  # pendiente

# =========================
# Procesamiento por día
# =========================
for archivo in archivos:
    df = pd.read_csv(archivo)
    fecha = archivo.stem

    x = df["tiempo_relativo_min"].values
    y_co2 = df["co2_ppm"].values
    y_ch4 = df["ch4_ppm"].values

    pendiente_co2 = calcular_pendiente(x, y_co2)
    pendiente_ch4 = calcular_pendiente(x, y_ch4)

    resultados.append({
        "fecha": fecha,
        "pendiente_co2": pendiente_co2,
        "pendiente_ch4": pendiente_ch4
    })

# =========================
# Crear DataFrame final
# =========================
df_resultados = pd.DataFrame(resultados)

# =========================
# Guardar
# =========================
df_resultados.to_csv(output_path, index=False)

# =========================
# Bitácora
# =========================
with open(bitacora_path, "a", encoding="utf-8") as f:
    f.write("\n\n## 04 - Cálculo de pendientes\n")
    f.write(f"- Fecha de ejecución: {datetime.now()}\n")
    f.write(f"- Carpeta de entrada: {input_dir}\n")
    f.write(f"- Archivo generado: {output_path}\n")

    f.write("- Método aplicado:\n")
    f.write("  - Regresión lineal (numpy.polyfit grado 1)\n")
    f.write("  - Cálculo de pendiente global por día\n")

    f.write(f"- Número de días procesados: {len(archivos)}\n")

    f.write("- Variables analizadas:\n")
    f.write("  - CO2 (ppm)\n")
    f.write("  - CH4 (ppm)\n")

    f.write("- Justificación técnica:\n")
    f.write("  La pendiente global permite cuantificar la tendencia general de las emisiones durante cada jornada, facilitando la comparación entre días.\n")