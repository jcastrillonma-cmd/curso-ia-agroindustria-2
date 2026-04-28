from pathlib import Path
import pandas as pd
from datetime import datetime

# =========================
# Definir raíz del proyecto
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

input_path = BASE_DIR / "data/raw/datosbase.csv"
output_path = BASE_DIR / "data/interim/datos_filtrados_ppm.csv"
bitacora_path = BASE_DIR / "reports/bitacora_limpieza.md"

# =========================
# 1. Lectura de datos
# =========================
df = pd.read_csv(input_path)

# =========================
# 2. Selección de columnas
# =========================
columnas_interes = ["created_at", "entry_id", "field2", "field4"]
df_filtrado = df[columnas_interes].copy()

# =========================
# 3. Renombrado
# =========================
df_filtrado.rename(columns={
    "field2": "co2_ppm",
    "field4": "ch4_ppm"
}, inplace=True)

# =========================
# 4. Conversión de fecha
# =========================
df_filtrado["created_at"] = pd.to_datetime(
    df_filtrado["created_at"],
    errors="coerce"
)

# =========================
# 5. Verificación básica
# =========================
nulos_fecha = df_filtrado["created_at"].isna().sum()

# =========================
# 6. Guardado
# =========================
df_filtrado.to_csv(output_path, index=False)

# =========================
# 7. Registro en bitácora
# =========================
with open(bitacora_path, "a", encoding="utf-8") as f:
    f.write("\n\n## 01 - Preparación de datos\n")
    f.write(f"- Fecha de ejecución: {datetime.now()}\n")
    f.write(f"- Archivo origen: {input_path}\n")
    f.write(f"- Archivo generado: {output_path}\n")
    f.write("- Transformaciones aplicadas:\n")
    f.write("  - Selección de columnas: created_at, entry_id, field2, field4\n")
    f.write("  - Eliminación de columnas no relevantes\n")
    f.write("  - Renombrado de variables:\n")
    f.write("      field2 → co2_ppm\n")
    f.write("      field4 → ch4_ppm\n")
    f.write("  - Conversión de created_at a datetime\n")
    f.write(f"- Registros con fecha inválida: {nulos_fecha}\n")
    f.write("- Justificación técnica:\n")
    f.write("  Se conservan únicamente las variables en ppm relevantes para el análisis de emisiones, garantizando consistencia y trazabilidad.\n")