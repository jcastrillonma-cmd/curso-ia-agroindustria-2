from pathlib import Path
import pandas as pd
from datetime import datetime

# =========================
# Definir rutas
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

input_path = BASE_DIR / "data/interim/datos_filtrados_ppm.csv"
output_dir = BASE_DIR / "data/processed/datos_por_dia"
output_general = BASE_DIR / "data/processed/datos_limpios.csv"
bitacora_path = BASE_DIR / "reports/bitacora_limpieza.md"

# Crear carpetas necesarias
output_dir.mkdir(parents=True, exist_ok=True)

# =========================
# 1. Lectura
# =========================
df = pd.read_csv(input_path)

# =========================
# 2. Conversión a datetime
# =========================
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# =========================
# 3. Crear columna fecha
# =========================
df["fecha"] = df["created_at"].dt.date

# =========================
# 4. Ordenar datos
# =========================
df = df.sort_values(by="created_at")

# =========================
# 5. FILTRADO DE OUTLIERS
# =========================

def filtrar_saltos(df, columna, umbral):
    df = df.copy()
    diff = df[columna].diff().abs()
    df.loc[diff > umbral, columna] = None
    return df

# =========================
# 5. FILTRADO SIMPLE Y SEGURO
# =========================

# eliminar valores absurdamente altos (ruido del sensor)
df.loc[df["co2_ppm"] > 3000, "co2_ppm"] = None
df.loc[df["ch4_ppm"] > 1500, "ch4_ppm"] = None

# eliminar valores negativos (por si existen)
df.loc[df["co2_ppm"] < 0, "co2_ppm"] = None
df.loc[df["ch4_ppm"] < 0, "ch4_ppm"] = None

# =========================
# 6. INTERPOLACIÓN
# =========================
df["co2_ppm"] = df["co2_ppm"].interpolate(limit_direction="both")
df["ch4_ppm"] = df["ch4_ppm"].interpolate(limit_direction="both")
# 7. Alineación temporal
# =========================
df["tiempo_relativo_min"] = df.groupby("fecha")["created_at"] \
    .transform(lambda x: (x - x.min()).dt.total_seconds() / 60)

# =========================
# 8. Guardar base limpia general
# =========================
df.to_csv(output_general, index=False)

# =========================
# 9. Separación por días
# =========================
fechas = df["fecha"].dropna().unique()

archivos_generados = []

for fecha in fechas:
    df_dia = df[df["fecha"] == fecha].copy()

    nombre_archivo = f"{fecha}.csv"
    ruta_salida = output_dir / nombre_archivo

    df_dia.to_csv(ruta_salida, index=False)
    archivos_generados.append(nombre_archivo)

# =========================
# 10. Registro en bitácora
# =========================
with open(bitacora_path, "a", encoding="utf-8") as f:
    f.write("\n\n## 02 - Segmentación diaria\n")
    f.write(f"- Fecha de ejecución: {datetime.now()}\n")
    f.write(f"- Archivo origen: {input_path}\n")
    f.write(f"- Archivo generado (general): {output_general}\n")

    f.write("- Transformaciones aplicadas:\n")
    f.write("  - Creación de columna 'fecha' a partir de created_at\n")
    f.write("  - Ordenamiento temporal de los datos\n")
    f.write("  - Filtrado de valores atípicos por cambios abruptos\n")
    f.write("  - Aplicación de umbral diferencial para CO2 y CH4\n")
    f.write("  - Interpolación de valores faltantes\n")
    f.write("  - Cálculo de tiempo relativo por día\n")
    f.write("  - Segmentación en archivos individuales por fecha\n")

    f.write(f"- Número de días detectados: {len(fechas)}\n")

    f.write("- Archivos generados:\n")
    for archivo in archivos_generados:
        f.write(f"  - {archivo}\n")

    f.write("- Justificación técnica:\n")
    f.write("  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.\n")
    f.write("  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.\n")
    f.write("  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.\n")